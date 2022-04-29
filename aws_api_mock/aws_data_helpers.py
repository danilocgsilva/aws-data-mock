import sys
import math
from random import random
import random as baserandom


def get_exadecimal_sample(num) -> str:
    possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hexadecimalcode = ""

    for x in range(num):
        hexadecimalcode += possibilities[math.floor(random() * len(possibilities))]

    return hexadecimalcode


def random_until_255() -> str:
    result_random = math.ceil(random() * 255)
    return str(result_random)


def random_until_n(n: int) -> int:
    result_random = math.ceil(random() * n)
    return result_random


def get_mac_address() -> str:
    mac_address_parts = []
    for x in range(6):
        mac_address_parts.append(get_exadecimal_sample(2))
    return ":".join(mac_address_parts)


def generate_owner_code() -> str:

    numbers_list = ["0","1","2","3","4","5","6","7","8","9"]
    owner_code = ""
    for i in range(12):
        owner_code += baserandom.choice(numbers_list)

    return owner_code


def generate_random_string_with_hard_chars(count: int) -> str:

    str_to_return = ""

    chars_colection = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "x", "z", "A",
        "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
        "Q", "R", "S", "R", "U", "V", "W", "Y", "Z", "=", "/", "+"]

    for i in range(count):
        str_to_return += baserandom.choice(chars_colection)

    return str_to_return

