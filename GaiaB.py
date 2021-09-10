import time
import random
import Gaialogic as glog
import data
import Move
import led

mve = Move.Move


def send_gl():
    glog.receive_gaia()


def critical_data_received(var):
    """
    :param var:
    """
    pass


def send_needs_charging():
    return glog.needscharging


def battery_charging():
    # TODO build charging code
    # if touch sinser is == 1:
    print("yes")
    if send_needs_charging() == 1 and is_charging() == 1:
        while data.send_mbatt() < 95 or data.send_cbatt() < 95:
            print("charging")
        ba = open('log.txt', "a")
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Charging Completed\n")
        ba.close()
        md = open('BatteryLogger.txt', "a")
        md.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Charging Completed\n")
        md.close()
        print('done')


def is_charging():
    ischbatt = 1
    if data.send_charge_touch() == 1 and ischbatt == 1:
        ba = open('log.txt', "a")
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Connected and charging\n")
        ba.close()
        return 1
    elif data.send_charge_touch() == 1 and ischbatt == 0:
        ba = open('Error.txt', "a")
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Connected but not charging\n")
        ba.close()
        return 2
    elif data.send_charge_touch() == 0 and ischbatt == 1:
        ba = open('Error.txt', "a")
        ba.write(time.strftime("%m/%d/%Y;%H:%M:%S:...") + "Charging but touch sensor failed\n")
        ba.close()
        return 3
    elif data.send_charge_touch() == 0 and ischbatt == 0:
        ba = open('log.txt', "a")
        ba.write(time.strftime("%m/%d/%Y;%H:%M:%S:...") + "Not Charging\n")
        ba.close()
        return 4


def legandpos(leg, posa):
    global pos
    pos = posa
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

    Exp: A= 1,2,3,4,5
    """
    if pos >= 2200 or pos <= 700:
        if pos >= 2200:
            pos = 2000
        elif pos <= 740:
            pos = 750

    return


class DailyRoutine:

    def __init__(self):
        pass

    def gettimeofday(self,ch):
        ltime = time.localtime()
        lhour = ltime.tm_hour
        lmin = ltime.tm_min
        if ch == 1:
        return lhour
        if ch == 2:
        
        print(lhour)


class MorningRoutine(DailyRoutine):

    def setmorningr(self):
        pass


class DayRoutine(DailyRoutine):

    def setdayr(self):
        pass


class NightRoutine(DailyRoutine):

    def setnightr(self):
        pass



if __name__ == '__main__':
    pass
