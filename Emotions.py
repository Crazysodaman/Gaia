import random
import filehandler as fh

class Emotions:

    def __init__(self):
        self.mhs = 50  # happy sad index (50 is neutral)
        self.mcm = 50  # calm mad index (50 is neutral)
        self.mgm = 50  # good mischief index (50 in neutral)

    def setneutral(self):
        self.mgm = 50
        self.mcm = 50
        self.mhs = 50

    def setneutralsave(self):
        self.mgm = 50
        self.mcm = 50
        self.mhs = 50
        fh.writedataa(self.mhs, "Emotions", "mhs")
        fh.writedataa(self.mgm, "Emotions", "mgm")
        fh.writedataa(self.mcm, "Emotions", "mcm")

    def readhappysad(self):
        return self.mhs

    def readcalmmad(self):
        return self.mcm

    def readgoodmischief(self):
        return self.mgm

    def filehappysad(self):

        return fh.readdataa("Emotions","mhs")

    def filecalmmad(self):
        return fh.readdataa("Emotions","mcm")

    def filegoodmischief(self):
        return fh.readdataa("Emotions","mgm")

    def savehappysad(self):
        return fh.writedataa(self.mhs, "Emotions", "mhs")

    def savecalmmad(self):
        return fh.writedataa(self.mcm, "Emotions", "mcm")

    def savegoodmis(self):
        return fh.writedataa(self.mgm, "Emotions", "mgm")

    def randommoodhappysad(self):
        self.mhs = random.randrange(0, 100, 5)
        fh.writedataa(self.mhs, "Emotions", "mhs")
        return self.mhs

    def randommoodcalmmad(self):
        self.mcm = random.randrange(0, 100, 5)
        return self.mcm

    def randommoodgoodmischief(self):
        self.mgm = random.randrange(0, 100, 5)
        return self.mgm

    def makehappysad(self, i):
        self.mhs = self.mhs + i
        fh.writedataa(self.mhs, "Emotions", "mhs")
        return self.mhs

    def makecalmmad(self, i):
        self.mcm = self.mcm + i
        fh.writedataa(self.mcm, "Emotions", "mcm")
        return self.mcm

    def makegoodmis(self, i):
        self.mgm = self.mgm + i
        fh.writedataa(self.mgm, "Emotions", "mgm")
        return self.mgm


class HappySad(Emotions):

    def __init__(self):
        super(HappySad, self).__init__()


class CalmMad(Emotions):

    def __init__(self):
        super(CalmMad, self).__init__()


class GoodMischief(Emotions):

    def __init__(self):
        super(GoodMischief, self).__init__()

if __name__ == '__main__':
    Emote=Emotions()
    Emote.setneutralsave()