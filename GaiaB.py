import time
import random
import threading as thread
import Gaialogic as glog
import data
import Move
import led
import Emotions

mve = Move.Move()
emot = Emotions.Emotions()


class Singleton(object):
    _instance = None
    _lock = thread.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Singleton, cls).__new__()
        return cls._instance


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


class DailyRoutine(Singleton):

    def __init__(self):
        self.mbr = 10  # Morning LED Brightness
        self.dbr = 13  # Day LED Brightness
        self.nbr = 5  # Night LED Brightness
        self.ledcolor = 0x0F000F  # LED Color


class MorningRoutine(DailyRoutine):

    def __init__(self):
        super(MorningRoutine, self).__init__()

    def __enter__(self):
        led.set_pixels(self.ledcolor, self.mbr)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        led.strip.clear_strip()

    def checkdate(self):
        pass


class DayRoutine(DailyRoutine):

    def __init__(self):
        super(DayRoutine, self).__init__()

    def __enter__(self):
        led.set_pixels(self.ledcolor, self.dbr)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        led.strip.clear_strip()

    def bored(self):
        pass


class NightRoutine(DailyRoutine):

    def __init__(self):
        super(NightRoutine, self).__init__()

    def __enter__(self):
        led.set_pixels(self.ledcolor, self.nbr)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        led.strip.clear_strip()

    def sleepy(self):
        pass


class RunRoutine(Singleton):

    def __init__(self):
        self.mr = MorningRoutine()
        self.dr = DayRoutine()
        self.nr = NightRoutine()
        self.mrs = 3  # Morning Speed
        self.drs = 2  # Day Speed
        self.nrs = 4  # Night Speed
        self.nmood = emot.setneutral()

    def gettimeofday(self, ch=1):
        ltime = time.localtime()
        lhour = ltime.tm_hour
        lmin = ltime.tm_min
        if ch == 1:
            return lhour
        elif ch == 2:
            return lmin

    def settimer(self):
        with self.mr as mr:
            while 6 <= self.gettimeofday() <= 10:
                led.strip.show()
                mve.stand(self.mrs)
                mr.checkdate()
        with self.dr as dr:
            while 11 <= self.gettimeofday() <= 18:
                led.strip.show()
                mve.stand(self.drs)
                dr.bored()
        with self.nr as nr:
            while self.gettimeofday() <= 5 or self.gettimeofday() >= 19:
                led.strip.show()
                mve.stand(self.nrs)
                nr.sleepy()


if __name__ == '__main__':
    pass
