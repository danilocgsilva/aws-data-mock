import math
from random import random

class GeneralDateUtilities:

    def getRandomYear(self) -> str:
        return str(math.ceil((random() * 10) + 2009))

    def getRandomMonth(self) -> str:
        return '{:02}'.format(math.ceil(random() * 12))

    def getRandomDay(self) -> str:
        return '{:02}'.format(math.ceil(random() * 28))

    def getRandomHour(self) -> str:
        return '{:02}'.format(math.floor(random() * 24))

    def getRandomMinuteOrSecond(self) -> str:
        return '{:02}'.format(math.floor(random() * 60))
