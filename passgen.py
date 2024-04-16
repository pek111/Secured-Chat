import random
import string
import msvcrt

from pyperclip import copy

def generate_password() -> str:
    password = []
    for _ in range(4):
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
    for _ in range(5):
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_lowercase))
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    pwd = generate_password()
    copy(pwd)
    print("Generated password copied to clipboard:", pwd)
    msvcrt.getch()
