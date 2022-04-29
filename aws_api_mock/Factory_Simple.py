from random import random
import math


class Factory_Simple:

    def __init__(self):
        self.possibles = []

    def set_possibles(self, possible):
        self.possibles.append(possible)
        return self

    def get_possibles(self) -> list:
        return self.possibles

    def get_extracting(self):
        possibles_length = len(self.possibles)
        if possibles_length == 0:
            raise Exception('There are no more elements to extract')
        choice_position = math.floor(random() * possibles_length)
        choice_result = self.possibles[choice_position]
        del self.possibles[choice_position]
        return choice_result
