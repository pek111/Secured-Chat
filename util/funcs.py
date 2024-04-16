import os

import rsa
import rsa.key
import maskpass

from msvcrt import getch

from urllib import request
from urllib.error import URLError

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher._mode_ctr import CtrMode

from password_strength import PasswordPolicy, PasswordStats
from password_strength.tests import (
    Length,
    Numbers,
    Special,
    Strength,
    Uppercase,
    EntropyBits
)

from util.assets import (
    unknown_ip_port,
    unknown_port,
    server_starting,
    client_connecting,
)

def clear() -> None :
    os.system("cls" if os.name == "nt" else "clear")

def c_exit(exit_code=0, clear_scr=False) -> None:
    if clear_scr:
        clear()
    print("\nPress any key to exit...", end="")
    getch()
    exit(exit_code)

def cn_exit(exit_code=0, clear_scr=False) -> None:
    if clear_scr:
        clear()
    print("\nPress any key two times to exit...", end="")
    getch()
    exit(exit_code)

def has_internet(with_cloudflare=True) -> bool:
    try:
        request.urlopen('https://8.8.8.8/', timeout=1) # Google DNS (Fast)
        return True
    except URLError: 
        if with_cloudflare:
            try:
                request.urlopen('https://1.1.1.1/', timeout=1.5) # Cloudflare DNS (Somewhat fast)
                return True
            except URLError:
                return False

def pass_stength(password: str) -> list:
    policy = PasswordPolicy.from_names(
        length=10,
        uppercase=2,
        numbers=2,
        special=2,
        entropybits=30,
        strength=0.45,
    )
    return policy.test(password)

def get_port() -> int:
    port = input()
    try:
        port = int(port)
    except ValueError:
        clear()
        print("\033[0mInvalid port.")
        c_exit(1)
        return -1

    if not 1 <= port <= 65535:
        clear()
        print("\033[0mInvalid port.")
        c_exit(1)
        return -1

    return port

def get_server_info() -> tuple[str, int, str]:
    clear()
    host = input(unknown_ip_port)

    if len(host) >= 15:
        alt_host = host[:12] + "..."
    else:
        alt_host = host

    clear()
    print(unknown_port.format(alt_host.center(19, " ")), end="")

    port = get_port()

    while True:
        clear()
        print(server_starting.format(alt_host.center(19, " "), str(port).center(19, " ")), end="")
        password = maskpass.askpass(prompt="\033[38;2;229;229;229m(Tip: Consider using a password generator or run passgen.py for a strong password)\nSet a password for this chat: \033[38;2;204;204;204m\033[2m")
        if password == "":
            print("\033[0m\033[38;2;241;76;76mPassword cannot be empty!")
            getch()
            continue
        elif pass_stength(password) != []:
            pastat = PasswordStats(password)

            if not Length(10).test(pastat):
                print("\033[0m\033[38;2;241;76;76mPassword must be at least 10 characters!\n\033[38;2;35;209;139m✓ ╶╴ helloworld\n\033[38;2;241;76;76m✗ ╶╴ hello")
            elif not Uppercase(2).test(pastat):
                print("\033[0m\033[38;2;241;76;76mPassword must contain at least two uppercase letters!\n\033[38;2;35;209;139m✓ ╶╴ HelloWorld\n\033[38;2;241;76;76m✗ ╶╴ helloworld")
            elif not Numbers(2).test(pastat):
                print("\033[0m\033[38;2;241;76;76mPassword must contain at least two numbers!\n\033[38;2;35;209;139m✓ ╶╴ H3lloW0rld\n\033[38;2;241;76;76m✗ ╶╴ HelloWorld")
            elif not Special(2).test(pastat):
                print("\033[0m\033[38;2;241;76;76mPassword must contain at least two special characters!\n\033[38;2;35;209;139m✓ ╶╴ #H3lloW0rld!\n\033[38;2;241;76;76m✗ ╶╴ H3lloW0rld")
            elif not EntropyBits(30).test(pastat):
                print("\033[0m\033[38;2;241;76;76mPassword needs more variety of characters!\n\033[38;2;35;209;139m✓ ╶╴ abC#H31loW0rld!@69420\n\033[38;2;241;76;76m✗ ╶╴ #H3lloW0rld!")
            elif not Strength(0.45).test(pastat):
                print("\033[0m\033[38;2;241;76;76mPassword is too weak!\n\033[38;2;35;209;139m✓ ╶╴ x[^1ed,.Dbi$(DlwAk8^\n\033[38;2;241;76;76m✗ ╶╴ qwertyuiop")

            getch()
            continue
        break

    print("\033[0m\033[38;2;229;229;229mServer started. Waiting for a connection...", end="", flush=True)

    return host, port, password

def get_host_info() -> tuple[str, int, str]:
    clear()
    host = input(unknown_ip_port)

    if len(host) >= 15:
        alt_host = host[:12] + "..."
    else:
        alt_host = host

    clear()
    print(unknown_port.format(alt_host.center(19, " ")), end="")

    port = get_port()

    clear()
    print(client_connecting.format(alt_host.center(19, " "), str(port).center(19, " ")), end="")
    
    password = maskpass.askpass(prompt="\033[38;2;229;229;229mEnter chat password: \033[38;2;204;204;204m\033[2m")

    return host, port, password

def setup_encryption() -> tuple[rsa.key.PublicKey, rsa.key.PrivateKey, bytes, CtrMode, bytes]:
    public_key, private_key = rsa.newkeys(1024)

    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_CTR)
    nonce = cipher.nonce

    return public_key, private_key, key, cipher, nonce

if __name__ == "__main__":
    print("This is a module. Import this module in main.py.")
