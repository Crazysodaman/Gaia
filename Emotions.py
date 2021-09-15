import random
from GaiaB import Singleton


class Emotions(Singleton):

    def __init__(self):
        self.mhs = 50  # happy sad index (50 is neutral)
        self.mcm = 50  # calm mad index (50 is neutral)
        self.mgm = 50  # good mischief index (50 in neutral)

    def setneutral(self):
        self.mgm = 50
        self.mcm = 50
        self.mhs = 50

    def readhappysad(self):
        return self.mhs

    def readcalmmad(self):
        return self.mcm

    def readrgoodmischief(self):
        return self.mgm

    def randommoodhappysad(self):
        self.mhs = random.randrange(0, 100, 5)
        return self.mhs

    def randommoodcalmmad(self):
        self.mcm = random.randrange(0, 100, 5)
        return self.mcm

    def randommoodgoodmischief(self):
        self.mgm = random.randrange(0, 100, 5)
        return self.mgm

    def makehappysad(self, i):
        self.mhs = self.mhs + i
        return self.mhs


class HappySad(Emotions):

    def __init__(self):
        super(HappySad, self).__init__()


class CalmMad(Emotions):

    def __init__(self):
        super(CalmMad, self).__init__()


class GoodMischief(Emotions):

    def __init__(self):
        super(GoodMischief, self).__init__()
