import time
import GaiaB
import serial
import Gaialogic as glog
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
touchcharge=1
needscharging=0
## ssc = serial.Serial("/dev/ttyUSB0", 115200, timeout=0);
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
    if cbatt <10 or mbatt <10:
        glog.low_battery()


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


def servomove(ms: int, *args: tuple) -> None:
    """
    Exmple: leg(100,(1,1500),(2,1500),(3,1500))
    :param ms: Time it has to move
    :param args: (# (servo), P(position))
    """
    command: str = ""
    for servo in args:
        command += f"#{servo[0]} P{servo[1]} "
    command += f"T{ms} \r"
    with serial.Serial("/dev/ttyUSB0", 115200, timeout=0) as ssc:
        ssc.write(command.encode())


def sendservopos(servo: tuple):
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
    #byt=len (servo)
    command = " "
    for serv in servo:
        command += "QP" + str(serv) + " "
    command += "\r"
    with serial.Serial("/dev/ttyUSB0", 115200, timeout=5) as ssc:
        ssc.write (command.encode())
        time.sleep(0.01)
        re=ssc.readall()
        rea=[]
        for letter in re:
            rea.append(letter *10)
        rea=tuple(rea)
        return rea


def allbullshit():
    return ACCx,ACCy,ACCz,GYRx,GYRy,GYRz,MAGx,MAGy,MAGz,kalmanY,kalmanX,tiltCompensatedHeading


if __name__ == '__main__':
<<<<<<< HEAD
    
    servomove(500,(3,2500),(15,1700),(6,500))
    A= (15,3,6)
    time.sleep(1)
    print (sendservopos(A))
=======

    change_mbatt(5)
    change_battery(5,5)
>>>>>>> c81293817b5001e8744d6d18babf5f2abe957aa7
