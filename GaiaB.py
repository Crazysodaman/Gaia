import time
import Gaialogic as glog
import data
import tensorflow as tefl

needscharging = 0


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


if __name__ == '__main__':
    pass
