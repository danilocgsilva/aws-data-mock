from random import random
import math
from awsapimock.GeneralDateUtilities import GeneralDateUtilities


class FullFormatDateMocking:

    def __init__(self):
        self.generalDateUtilities = GeneralDateUtilities()

    def getRandomTimeStringZ(self) -> str:
        return self.generalDateUtilities.getRandomYear() + "-" +\
            self.generalDateUtilities.getRandomMonth() + "-" +\
            self.generalDateUtilities.getRandomDay() + "T" + \
            self.generalDateUtilities.getRandomHour() + ":" +\
            self.generalDateUtilities.getRandomMinuteOrSecond() + ":" + \
            self.generalDateUtilities.getRandomMinuteOrSecond()+ ".000Z"

    def getRandomTimeStringGMT(self) -> str:
        return self.generalDateUtilities.getRandomYear() + "-" +\
            self.generalDateUtilities.getRandomMonth() + "-" +\
            self.generalDateUtilities.getRandomDay() + " " +\
            self.generalDateUtilities.getRandomDay() + ":" +\
            self.generalDateUtilities.getRandomMinuteOrSecond() + ":" +\
            self.generalDateUtilities.getRandomMinuteOrSecond() + " GMT" 
