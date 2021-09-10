import random
from GaiaB import Singleton


class Emotions(Singleton):

    def __init__(self):
        self.rmmhs = 50  # happy sad index (50 is neutral)
        self.rmmcm = 50  # calm mad index (50 is neutral)
        self.rmmgm = 50  # good mischief index (50 in neutral)

    def randommoodhappysad(self):
        self.rmmhs = random.randrange(0, 100, 5)
        return self.rmmhs

    def randommoodcalmmad(self):
        self.rmmcm = random.randrange(0, 100, 5)
        return self.rmmcm

    def randommoodgoodmischief(self):
        self.rmmgm = random.randrange(0, 100, 5)
        return self.rmmgm


class HappySad(Emotions):

    def __init__(self):
        pass


class CalmMad(Emotions):

    def __init__(self):
        pass


class GoodMischief(Emotions):

    def __init__(self):
        pass
