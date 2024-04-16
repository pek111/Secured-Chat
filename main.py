import rsa

import time
import socket
import threading

from util.pyarg import make_hash
from Crypto.Cipher import AES

from util.assets import (
    menu_prompt,
    client_connected,
    client_failed_intrnt,
    client_failed_no_intrnt,
    server_bad_ip_or_port,
    server_no_intrnt,
    help_cmd,
)

from util.funcs import (
    clear,
    c_exit,
    cn_exit,
    has_internet,
    get_server_info,
    get_host_info,
    setup_encryption,
)

MSG_START = b"<MSGSTART>"
SIG_END = b"<SIGEND>"
MSG_END = b"<MSGEND>"
INVLD_PASS = b"<INVLDPASS>"
PASS_OK = b"<PASSOK>"

public_key, private_key, key, cipher, nonce = setup_encryption()

clear()

choice = input(menu_prompt)
chat_history = client_connected

if choice == "1":
    host, port, password = get_server_info()
    pass_hash = make_hash(password, host, str(port)).encode()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((host, port))
        server.listen()
    except socket.gaierror:
        clear()
        if has_internet():
            print(server_bad_ip_or_port)
        else:
            print(server_no_intrnt)
        c_exit(1)
    except OSError:
        clear()
        print(server_bad_ip_or_port)
        c_exit(1)

    while True:
        client, _ = server.accept()

        client.send(public_key.save_pkcs1("PEM"))
        public_partner_key = rsa.PublicKey.load_pkcs1(client.recv(1024))

        client.send(rsa.encrypt(key, public_partner_key))
        partner_aes_key = rsa.decrypt(client.recv(1024), private_key)

        client.send(rsa.encrypt(nonce, public_partner_key))
        partner_aes_nonce = rsa.decrypt(client.recv(1024), private_key)

        partner_cipher = AES.new(partner_aes_key, AES.MODE_CTR, nonce=partner_aes_nonce)

        recv_pass_hash = partner_cipher.decrypt(client.recv(1024))
        if recv_pass_hash == pass_hash:
            client.send(PASS_OK)
            break
        client.send(INVLD_PASS)
        client.close()

    clear()
    print(chat_history)
elif choice == "2":
    host, port, password = get_host_info()
    pass_hash = make_hash(password, host, str(port)).encode()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
    except socket.gaierror:
        clear()
        if has_internet():
            print(client_failed_intrnt)
        else:
            print(client_failed_no_intrnt)
        c_exit(1)

    public_partner_key = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))

    partner_aes_key = rsa.decrypt(client.recv(1024), private_key)
    client.send(rsa.encrypt(key, public_partner_key))

    partner_aes_nonce = rsa.decrypt(client.recv(1024), private_key)
    client.send(rsa.encrypt(nonce, public_partner_key))

    partner_cipher = AES.new(partner_aes_key, AES.MODE_CTR, nonce=partner_aes_nonce)

    client.send(cipher.encrypt(pass_hash))
    if client.recv(1024) == INVLD_PASS:
        clear()
        print("\033[0m\033[38;2;241;76;76mIncorrect password! Please try again.\033[0m")
        c_exit(1)

    clear()
    print(chat_history)
else:
    clear()
    print("\033[0mInvalid choice.")
    c_exit(1)

def send_msg(c: socket.socket) -> None:
    global chat_history
    while True:
        message = input("      \033[0m\033[38;2;229;229;229m>>> ")
        if message in ["/", "/?", "/help"]:
            clear()
            print(chat_history)
            print(help_cmd)
            continue
        elif message == "/exit":
            c.close()
            cn_exit(0)
            break
        elif message == "\"\"\"":
            message = input("      \033[0m\033[38;2;229;229;229m... ")
            while True:
                line = input("      \033[0m\033[38;2;229;229;229m... ")
                if line == "\"\"\"":
                    break
                message += "\n          " + line
        enc_msg = cipher.encrypt(message.encode())
        try:
            c.send(MSG_START)
            c.send(rsa.sign(enc_msg, private_key, "SHA-512"))
            c.send(SIG_END)
            time.sleep(0.1)
            c.send(enc_msg)
            c.send(MSG_END)
        except ConnectionResetError:
            c.close()
            break
        except OSError:
            c.close()
            break
        chat_history += "\n\033[0m\033[48;2;35;209;139m\033[38;2;0;0;0m\033[1m   You   \033[0m \033[38;2;229;229;229m" + message
        clear()
        print(chat_history)

def recv_msg(c: socket.socket) -> None:
    global chat_history
    while True:
        try:
            data = c.recv(1024)
            if data == MSG_START:
                encrypted_message = b""
                signature = b""
                while True:
                    signature += c.recv(1024)
                    if SIG_END in signature:
                        signature = signature[:-len(SIG_END)]
                        break
                while True:
                    encrypted_message += c.recv(1024)
                    if MSG_END in encrypted_message:
                        encrypted_message = encrypted_message[:-len(MSG_END)]
                        break
                try:
                    rsa.verify(encrypted_message, signature, public_partner_key)
                except rsa.VerificationError:
                    chat_history += "\n\033[0m\033[48;2;245;245;67m\033[38;2;0;0;0m\033[1m Control \033[0m \033[38;2;229;229;229mPartner sent an invalid message."
                    clear()
                    print(chat_history)
                    continue
            message = partner_cipher.decrypt(encrypted_message).decode()
        except ConnectionResetError:
            print("\n\033[0m\033[48;2;245;245;67m\033[38;2;0;0;0m\033[1m Control \033[0m \033[38;2;229;229;229mPartner disconnected.\033[0m")
            c.close()
            cn_exit(0)
        except OSError:
            print("\n\033[0m\033[48;2;245;245;67m\033[38;2;0;0;0m\033[1m Control \033[0m \033[38;2;229;229;229mPartner disconnected.\033[0m")
            c.close()
            cn_exit(0)
        chat_history += "\n\033[0m\033[48;2;59;142;234m\033[38;2;0;0;0m\033[1m Partner \033[0m \033[38;2;229;229;229m" + message
        clear()
        print(chat_history)

threading.Thread(target=send_msg, args=(client,)).start()
threading.Thread(target=recv_msg, args=(client,)).start()
