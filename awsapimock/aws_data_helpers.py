import sys
import math
from random import random


def get_exadecimal_sample(num) -> str:
    possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hexadecimalcode = ""

    for x in range(num):
        hexadecimalcode += possibilities[math.floor(random() * len(possibilities))]

    return hexadecimalcode


def random_until_255() -> str:
    result_random = math.ceil(random() * 255)
    return str(result_random)
