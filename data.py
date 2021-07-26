import time
import GaiaB

cbatt = 0  # 1
mbatt = 0  # 2
ACCx = 0
ACCy = 0
ACCz = 0
GYRx = 0
GYRy = 0
GYRz = 0
MAGx = 0
MAGy = 0
MAGz = 0
kalmanY = 0
kalmanX = 0
tiltCompensatedHeading= 0
ischbatt=0
touchcharge=0
needscharging=0
def send_cbatt():
    return cbatt


def change_cbatt(data):
    global cbatt
    cbatt = data
    if cbatt %5 ==0:
        ba = open('BatteryLogger.txt', "a")
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ")+ "Computer Battery ")
        ba.writelines(str(cbatt)+" %\n")
        ba.close()
    elif cbatt <10:
        GaiaB.low_battery(1)


def send_mbatt():
    return mbatt


def change_mbatt(data):
    global mbatt
    mbatt = data
    if mbatt %5 ==0:
        ba = open('BatteryLogger.txt', "a")
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S:")+ "Motor Battery ")
        ba.writelines(str(mbatt)+" %\n")
        ba.close()
    elif mbatt <10:
        GaiaB.low_battery(2)


def change_battery(data1,data2):
    """
    :param data1: CBatt
    :param data2: MBatt
    """
    global mbatt
    global cbatt
    cbatt = data1
    mbatt = data2
    ba = open('BatteryLogger.txt', "a")
    if cbatt %5 ==0 and mbatt %5==0:
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ")+ "Computer Battery ")
        ba.writelines(str(cbatt)+" %\n")
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S:") + "Motor Battery ")
        ba.writelines(str(mbatt) + " %\n")
        ba.close()
    elif cbatt %5 ==0:
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S: ")+ "Computer Battery ")
        ba.writelines(str(cbatt)+" %\n")
        ba.close()
    elif mbatt %5 ==0:
        ba.write(time.strftime("%m/%d/%Y %H:%M:%S:")+ "Motor Battery ")
        ba.writelines(str(mbatt)+" %\n")
        ba.close()
    elif cbatt <10 or mbatt <10:
        GaiaB.low_battery()


def send_charge_touch():
    return touchcharge

def ACCx_change(data):
    global ACCx
    ACCx=data


def ACCy_change(data):
    global ACCy
    ACCy=data


def ACCz_change(data):
    global ACCz
    ACCz=data


def GYRx_change(data):
    global GYRx
    GYRx = data


def GYRy_change(data):
    global GYRy
    GYRy = data


def GYRz_change(data):
    global GYRz
    GYRz = data


def MAGx_change(data):
    global MAGx
    MAGx = data


def MAGy_change(data):
    global MAGy
    MAGy = data


def MAGz_change(data):
    global MAGz
    MAGz = data


def kalmanY_change(data):
    global kalmanY
    kalmanY = data


def kalmanX_change(data):
    global kalmanX
    kalmanX = data

def tiltCompensatedHeading_change(data):
    global tiltCompensatedHeading
    tiltCompensatedHeading = data


def ACCx_send():
    return ACCx


def ACCy_send():
    return ACCy


def ACCz_send():
    return ACCz


def GYRx_send():
    return GYRx


def GYRy_send():
    return GYRy


def GYRz_send():
    return GYRz


def MAGx_send():
    return MAGx


def MAGy_send():
    return MAGy


def MAGz_send():
    return MAGz


def kalmanY_send():
    return kalmanY


def kalmanX_send():
    return kalmanX

def tiltCompensatedHeading_send():
    return tiltCompensatedHeading

def allbullshit():
    return ACCx,ACCy,ACCz,GYRx,GYRy,GYRz,MAGx,MAGy,MAGz,kalmanY,kalmanX,tiltCompensatedHeading


if __name__ == '__main__':

    change_battery(5,6)