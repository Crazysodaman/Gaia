import data
import random
import time


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

       servo positions:
       750 Low
       1500 Middle (default)
       2500 High
       """

    def __init__(self):
        self.ssc = data.SSC32()
        self.aspr = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # all servo positions right
        self.aspl = [16, 17, 18, 19, 20, 21, 22, 23, 24]  # all servo positions left
        self.gar = [2, 21, 8]
        self.gat = [1, 20, 7]
        self.gaf = [0, 19, 6]
        self.gbr = [24, 5, 18]
        self.gbt = [23, 4, 17]
        self.gbf = [22, 3, 16]
        self.frr = [8]
        self.frt = [7]
        self.frft = [6]
        self.crr = [5]
        self.crt = [4]
        self.crft = [3]
        self.brr = [2]
        self.brt = [1]
        self.brft = [0]
        self.flr = [24]
        self.flt = [23]
        self.flft = [22]
        self.clr = [21]
        self.clt = [20]
        self.clft = [19]
        self.blr = [18]
        self.blt = [17]
        self.blft = [16]

    def setspeed(self, ch):
        """
        :param ch: 1:Fast 2:FMid 3:Mid 4:SMid 5:Slow
        :return: set speed
        """
        if ch == 1:  # Fast
            return 100
        if ch == 2:  # FMid
            return 250
        if ch == 3:  # Mid
            return 500
        if ch == 4:  # SMid
            return 750
        if ch == 5:  # Slow
            return 1000

    def randomspeed(self, ch):
        """
        :param ch: 1:Any 2:Fast 3:FMid 4:SMid 5:Slow
        :return: Random speed
        """
        if ch == 1:  # full range
            return random.randrange(100, 1000, 10)
        if ch == 2:  # Fast
            return random.randrange(100, 250, 10)
        if ch == 3:  # FMid
            return random.randrange(250, 500, 10)
        if ch == 4:  # SMid
            return random.randrange(500, 750, 10)
        if ch == 5:  # Slow
            return random.randrange(750, 1000, 10)

    def servofilter(self, servo, pos, xpwm, ch=1):
        """
        :param servo: what servos
        :param pos: what position
        :param xpwm: position you want
        :param ch: what you want returned 1:servos 2:position 3:both
        """
        srvo = []
        pwm = []
        srvoapwn = []
        for i in zip(servo, pos):
            if xpwm - i[1] == 0:
                continue
            srvo.append(i[0])
            pwm.append(i[1])
            srvoapwn.append(i)
        if ch == 1:
            return srvo
        if ch == 2:
            return pwm
        if ch == 3:
            return srvoapwn

    def posmaker(self, servo, pos):
        """
        :param servo: any
        :param pos: 1500 is default
        :return: a list of pos ex: 1500,1500
        """
        pwm = []
        for i in range(len(servo)):
            pwm.append(pos)
        return pwm

    def posmakera(self, servo, posa, posb):
        """
        :param servo: any
        :param posa: 1500 is default
        :param posb: exp 750
        :return: a list of pos ex: 1500,750,1500
        """
        pwm = []
        for i in range(len(servo)):
            if i % 2 == 0:
                pwm.append(posa)
            else:
                pwm.append(posb)
        return pwm

    def stand(self, ch):
        """
        :param ch: 1:Any 2:Fast 3:Mid 4:Slow
        :return: speed
        """
        ms = self.randomspeed(ch)
        aspr1 = self.ssc.sendservopos(self.aspr)
        aspl1 = self.ssc.sendservopos(self.aspl)
        aspr2 = self.servofilter(self.aspr, aspr1, 1500)
        aspl2 = self.servofilter(self.aspr, aspl1, 1500)
        aspr3 = self.posmaker(aspr2, 1500)
        aspl3 = self.posmaker(aspl2, 1500)
        self.ssc.servomove(ms, aspr2, aspr3)
        self.ssc.servomove(ms, aspl2, aspl3)

    def forward(self, ch, Tt):
        """
        :param ch: 1:Any 2:Fast 3:Mid 4:Slow
        :param T: how long it will go forward
        :return: speed
        """
        ms = self.randomspeed(ch)
        self.stand(ch)
        gat1 = self.posmaker(self.gat, 1500)  # legs default A
        gat2 = self.posmakera(self.gat, 1250, 1750)  # up A
        gar1 = self.posmaker(self.gar, 1500)  # legs default A
        gar2 = self.posmakera(self.gar, 900, 2100)  # move A
        gbt1 = self.posmaker(self.gbt, 1500)  # legs default B
        gbt2 = self.posmakera(self.gbt, 1750, 1250)  # up B
        gbr1 = self.posmaker(self.gbr, 1500)  # legs default B
        gbr2 = self.posmakera(self.gbr, 2100, 900)  # move B

        t_end = time.time() + Tt
        while time.time() < t_end:
            self.ssc.servomove(ms, self.gat, gat2)
            while self.ssc.sendservopos(self.gat) != gat2:
                continue  # up A
            self.ssc.servomove(ms, self.gar, gar2)
            while self.ssc.sendservopos(self.gar) != gar2:
                continue  # Move A
            self.ssc.servomove(ms, self.gat, gat1)
            while self.ssc.sendservopos(self.gat) != gat1:
                continue  # Down A
            self.ssc.servomove(ms, self.gbt, gbt2)
            while self.ssc.sendservopos(self.gbt) != gbt2:
                continue  # up B
            self.ssc.servomove(ms, self.gar, gar1)
            while self.ssc.sendservopos(self.gar) != gar1:
                continue  # Move A
            self.ssc.servomove(ms, self.gbr, gbr2)
            while self.ssc.sendservopos(self.gbr) != gbr2:
                continue  # Move B
            self.ssc.servomove(ms, self.gbt, gbt1)
            while self.ssc.sendservopos(self.gbt) != gbt1:
                continue  # Down B
            self.ssc.servomove(ms, self.gat, gat2)
            while self.ssc.sendservopos(self.gat) != gat2:
                continue  # up A
            self.ssc.servomove(ms, self.gbr, gbr1)
            while self.ssc.sendservopos(self.gbr) != gbr1:
                continue  # Move B
        self.stand(ch)

    def backward(self):
        self.stand()
        pass

    def left(self):
        self.stand()
        pass

    def right(self):
        self.stand()
        pass
