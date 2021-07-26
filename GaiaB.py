import time
import Gaialogic as glog
import data

def send_gl():
    glog.receive_gaia()

def critical_data_received(var):
    """
    :param var:
    """
    pass

def low_battery():
    mf = open('log.txt', "a")
    if data.send_cbatt() < 10 and data.send_mbatt() < 10:
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Computer Battery Low \n")
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Motor Battery Low \n")
        mf.close()
    elif data.send_cbatt() < 10:
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Computer Battery Low \n")
        mf.close()
    elif data.send_mbatt() < 10:
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Motor Battery Low \n")
        mf.close()
    print("yes")
    change_needs_charging(1)


def battery_charging():
    #TODO build charging code
    #if touch sinser is == 1:
    print("yes")
    if send_needs_charging()==1:
        while True:
            if data.send_cbatt()>95 and data.send_mbatt()>95:
                ba = open('log.txt', "a")
                ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Charging Completed\n")
                ba.close()
                ba = open('BatteryLogger.txt', "a")
                ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Charging Completed\n")
                ba.close()
                print ('done')
                break
            elif data.send_mbatt() <95 or data.send_cbatt() <95:
                print ('charging')

def is_charging():
    touchcharge =1
    ischbatt=1
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

def change_needs_charging(data):
    global needscharging
    needscharging=data

def send_needs_charging():
    return needscharging

if __name__ == '__main__':
    pass