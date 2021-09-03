import data

ssc = data.SSC32()
aspr = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # all servo positions right
aspl = [16, 17, 18, 19, 20, 21, 22, 23, 24]  # all servo positions left
gar = [2, 21, 8]
gat = [1, 20, 7]
gaf = [0, 19, 6]
gbr = [24, 5, 18]
gbt = [23, 4, 17]
gbf = [22, 3, 16]
frr = [8]
frt = [7]
frft = [6]
crr = [5]
crt = [4]
crft = [3]
brr = [2]
brt = [1]
brft = [0]
flr = [24]
flt = [23]
flft = [22]
clr = [21]
clt = [20]
clft = [19]
blr = [18]
blt = [17]
blft = [16]


class Move:
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

    def __init__(self):
        pass

    def servofilter(self, servo, pos, xpwm, ch=1):
        """
        :param servo: what servos
        :param pos: what position
        :param xpwm: position you want
        :param ch: what you want returned 1:servos 2:position 3:both
        """
        srvo=[]
        pwm=[]
        srvoapwn=[]
        for i in zip(servo, pos):
            if xpwm - i[1] == 0:
                continue
            srvo.append(i[0])
            pwm.append(i[1])
            srvoapwn.append(i)
        if ch ==1:
            return srvo
        if ch ==2:
            return pwm
        if ch ==3:
            return srvoapwn

    def posmaker(self, servo, pos):
        pwm=[]
        for i in range(len(servo)):
            pwm.append(pos)
            return pwm

    def stand(self,ms):
        aspr1 = ssc.sendservopos(aspr)
        aspl1 = ssc.sendservopos(aspl)
        aspr2=self.servofilter(aspr, aspr1, 1500)
        aspl2 = self.servofilter(aspr, aspl1, 1500)
        aspr3= self.posmaker(aspr2,1500)
        aspl3 = self.posmaker(aspl2, 1500)
        ssc.servomove(ms,aspr2, aspr3)
        ssc.servomove(ms,aspl2, aspl3)

    def forward(self):
        self.stand()
        brrpos = self.posmaker(brr, 2000)
        ssc.servomove(100, brr, brrpos)
        while ssc.sendservopos(brr) != brrpos:
            continue
        brrpos= self.posmaker(brr, 1000)
        ssc.servomove(100, brr, brrpos)
        while ssc.sendservopos(brr) != brrpos:
            continue


    def backward(self):
        self.stand()
        pass

    def left(self):
        self.stand()
        pass

    def right(self):
        self.stand()
        pass
d=[1,2,3,4,5,6,7,8,9]
Move.servofilter(aspl,d)