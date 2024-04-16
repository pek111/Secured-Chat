import random
import pyargon2

def arg_hash(password: str, salt: str, pepper: str) -> str:
    pass_hash = pyargon2.hash(password, salt, pepper, time_cost=512)
    return pass_hash

def make_hash(password: str, host: str, port: str) -> str:
    salt = password + port + host + port[::-1]*2 + host[::-1]*3
    pepper = port[::-1]*3 + host + password*2 + port + host[::-1]*2

    random.seed(salt + pepper + password)
    salt = [char for char in salt]
    pepper = [char for char in pepper]
    random.shuffle(salt)
    random.shuffle(pepper)

    final_hash = arg_hash(password, "".join(salt)[::-1], "".join(pepper)[::-1])
    return final_hash

if __name__ == "__main__":
    print("This is a module. Import this module in main.py.")
