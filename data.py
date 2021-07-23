import time
cbatt = 4  # 1
mbatt = 23  # 2
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

def send_cbatt():
    return cbatt


def change_cbatt(data):
    global cbatt
    cbatt = data


def send_mbatt():
    return mbatt


def change_mbatt(data):
    global mbatt
    mbatt = data
    if mbatt %5 ==0:
        ba = open('BatteryLogger.txt', "a")
        ba.write(time.strftime("%B/%d/%Y;%H:%M:%S:...")+ "Motor Battery ")
        ba.writelines(str(mbatt)+" %\n")
        ba.close()



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

def allbullshit():
    return ACCx,ACCy,ACCz,GYRx,GYRy,GYRz,MAGx,MAGy,MAGz,kalmanY,kalmanX,tiltCompensatedHeading

change_mbatt(30)