import data

ssc = data.SSC32()
aspr = (0, 1, 2, 3, 4, 5, 6, 7, 8)  # all servo positions right
aspl = (16, 17, 18, 19, 20, 21, 22, 23, 24)  # all servo positions left
gar = (2, 21, 8)
gat = (1, 20, 7)
gaf = (0, 19, 6)
gbr = (24, 5, 18)
gbt = (23, 4, 17)
gbf = (22, 3, 16)
frr = (8,)
frt = (7,)
frft = (6,)
crr = (5,)
crt = (4,)
crft = (3,)
brr = (2,)
brt = (1,)
brft = (0,)
flr = (24,)
flt = (23,)
flft = (22,)
clr = (21,)
clt = (20,)
clft = (19,)
blr = (18,)
blt = (17,)
blft = (16,)


class Move():
    """
       servo and numbers
       FRR-8   FLR-24
       FRT-7   FLT-23
       FRFT-6  FLFT-22
       CRR-5   CLR-21
       CRT-4   CLT-20
       CRFT-3  CLFT-19
       BRR-2   BLR-18
       BRT-1   BLT-17
       BRFT-0  BLFT-16

       leg groups
       A (8,7,6),(21,20,19),(2,1,0)
       B (24,23,22),(5,4,3),(18,17,16)
       """

    def __init__(self,ms=None):
        self.ms = ms

    def stand(self):

        ssc.servomove(self.ms,)
        ssc.servomove(self.ms,)

    def forward(self):
        sspr = ssc.sendservopos(aspr)
        sspl = ssc.sendservopos(aspl)
        ssc.servomove(self.ms, )
        pass

    def backward(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

ssc.servomove(1, ()