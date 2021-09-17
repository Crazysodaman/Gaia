import data
import random
import time


class Move:
    """
    Handles all Servos
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

    def highapos(self, ch=4):
        """
        Range of motion for servo group A
        :param ch: 1:full 2: Short 3: Mid 4:Long
        :return:
        """
        if ch == 1:  # full range
            return random.randrange(1600, 2500, 10)
        if ch == 2:  # Short
            return random.randrange(1600, 1900, 10)
        if ch == 3:  # Mid
            return random.randrange(1900, 2100, 10)
        if ch == 4:  # Long
            return random.randrange(2100, 2500, 10)

    def highbpos(self, ch=4):
        """
        Range of motion for servo group B
        :param ch: 1:full 2: Short 3: Mid 4:Long
        """
        if ch == 1:  # full range
            return random.randrange(750, 1400, 10)
        if ch == 2:  # Short
            return random.randrange(1200, 1400, 10)
        if ch == 3:  # Mid
            return random.randrange(900, 1200, 10)
        if ch == 4:  # Long
            return random.randrange(750, 900, 10)

    def rotateapos(self, ch=4):
        """
        Range of motion for servo group B
        :param ch: 1:full 2: Short 3: Mid 4:Long
        """
        if ch == 1:  # full range
            return random.randrange(800, 1400, 10)
        if ch == 2:  # Short
            return random.randrange(1200, 1400, 10)
        if ch == 3:  # Mid
            return random.randrange(1000, 1200, 10)
        if ch == 4:  # Long
            return random.randrange(800, 1000, 10)

    def rotatebpos(self, ch=4):
        """
        Range of motion for servo group B
        :param ch: 1:full 2: Short 3: Mid 4:Long
        """
        if ch == 1:  # full range
            return random.randrange(1600, 2200, 10)
        if ch == 2:  # Short
            return random.randrange(1600, 1800, 10)
        if ch == 3:  # Mid
            return random.randrange(1800, 2000, 10)
        if ch == 4:  # Long
            return random.randrange(2000, 2200, 10)

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
        elif ch == 2:
            return pwm
        elif ch == 3:
            return srvoapwn

    def servolistfilter(self, servo, pos, xpwm):
        out = []
        for current_pos, desired_pos, servo in zip(pos, xpwm, servo):
            if current_pos != desired_pos:
                out.append(servo)
        return out

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

    def testoneservo(self, servo, pos=1500, ms=500):
        self.ssc.testmove(ms, servo, pos)
        while self.ssc.sendservopos(servo) != pos:
            break

    def testservos(self, servo, posa, posb, ms=500):
        posm = self.posmakera(servo, posa, posb)
        self.ssc.servomove(ms, servo, posm)
        time.sleep(2)
        srvo = self.ssc.sendservopos(servo)
        return self.servolistfilter(servo, srvo, posm)

    def stand(self, ch):
        """
        :param ch: 1:Any 2:Fast 3:Mid 4:Slow
        :return: speed
        """
        ms = self.randomspeed(ch)
        aspr1 = self.ssc.sendservopos(self.aspr)
        aspl1 = self.ssc.sendservopos(self.aspl)
        aspr2 = self.servofilter(self.aspr, aspr1, 1500)
        aspl2 = self.servofilter(self.aspl, aspl1, 1500)
        aspr3 = self.posmaker(aspr2, 1500)
        aspl3 = self.posmaker(aspl2, 1500)
        self.ssc.servomove(ms, aspr2, aspr3)
        self.ssc.servomove(ms, aspl2, aspl3)

    def forward(self, tt, ch=1, ch1=1, ch2=1750, ch3=1250, ch4=900, ch5=2100):
        """
        :param tt: how long it will go forward
        :param ch: 0- random 1-fixed
        :param ch1: Speed of servo 1:Any 2:Fast 3:Mid 4:Slow or 50
        :param ch2: leg HighA 1:Any 2:Short 3:Mid 4:Long or 1750
        :param ch3: leg HighB 1:Any 2:Short 3:Mid 4:Long or 1250
        :param ch4: rotate A 1:Any 2:Short 3:Mid 4:Long or 900
        :param ch5: rotate B 1:Any 2:Short 3:Mid 4:Long or 2100
        :return: speed
        """
        global rotatea, rotateb, highb, higha, ms
        cntr = 1500
        if ch == 0:
            ms = self.randomspeed(ch1)
            higha = self.highapos(ch2)
            highb = self.highbpos(ch3)
            rotatea = self.rotateapos(ch4)
            rotateb = self.rotatebpos(ch5)
        elif ch == 1:
            ms = self.setspeed(ch1)
            higha = ch2
            highb = ch3
            rotatea = ch4
            rotateb = ch5

        self.stand(ch)
        time.sleep(0.2)
        gat1 = self.posmaker(self.gat, cntr)  # legs default A
        gat2 = self.posmakera(self.gat, highb, higha)  # up A
        gar1 = self.posmaker(self.gar, cntr)  # legs default A
        gar2 = self.posmakera(self.gar, rotatea, rotateb)  # move A
        gbt1 = self.posmaker(self.gbt, cntr)  # legs default B
        gbt2 = self.posmakera(self.gbt, higha, highb)  # up B
        gbr1 = self.posmaker(self.gbr, cntr)  # legs default B
        gbr2 = self.posmakera(self.gbr, rotateb, rotatea)  # move B

        t_end = time.time() + tt
        while time.time() < t_end:
            self.ssc.servomove(ms, self.gat, gat2)
            while self.ssc.sendservopos(self.gat) != gat2:
                break  # up A
            self.ssc.servomove(ms, self.gar, gar2)
            while self.ssc.sendservopos(self.gar) != gar2:
                break  # Move A
            self.ssc.servomove(ms, self.gat, gat1)
            while self.ssc.sendservopos(self.gat) != gat1:
                break  # Down A
            self.ssc.servomove(ms, self.gbt, gbt2)
            while self.ssc.sendservopos(self.gbt) != gbt2:
                break  # up B
            self.ssc.servomove(ms, self.gar, gar1)
            while self.ssc.sendservopos(self.gar) != gar1:
                break  # Move A
            self.ssc.servomove(ms, self.gbr, gbr2)
            while self.ssc.sendservopos(self.gbr) != gbr2:
                break  # Move B
            self.ssc.servomove(ms, self.gbt, gbt1)
            while self.ssc.sendservopos(self.gbt) != gbt1:
                break  # Down B
            self.ssc.servomove(ms, self.gat, gat2)
            while self.ssc.sendservopos(self.gat) != gat2:
                break  # up A
            self.ssc.servomove(ms, self.gbr, gbr1)
            while self.ssc.sendservopos(self.gbr) != gbr1:
                break  # Move B
        self.stand(ch)

    def backward(self, ch):
        self.stand(ch)
        pass

    def left(self, ch):
        self.stand(ch)
        pass

    def right(self, ch):
        self.stand(ch)


if __name__ == '__main__':
    mve = Move()
    mve.stand(1)
    mve.forward(20, 0, 1, 1, 1, 1, 1)
