import smbus
bus = smbus.SMBus(1)
from LSM9DS1 import *
import time



def writeAG(register,value):
    bus.write_byte_data(ACC_ADDRESS , register, value)
    return -1

def writeACC(register,value):
    bus.write_byte_data(ACC_ADDRESS , register, value)
    return -1

def writeMAG(register,value):
    bus.write_byte_data(MAG_ADDRESS, register, value)
    return -1

def writeGRY(register,value):
    bus.write_byte_data(GYR_ADDRESS, register, value)
    return -1





def writeACC(register,value):
    bus.write_byte_data(LSM9DS1_ACC_ADDRESS , register, value)
    return -1


def writeMAG(register,value):
    bus.write_byte_data(LSM9DS1_MAG_ADDRESS , register, value)
    return -1

def writeGRY(register,value):
    bus.write_byte_data(LSM9DS1_GYR_ADDRESS , register, value)
    return -1



def readACCx():
    acc_l = bus.read_byte_data(LSM9DS1_ACC_ADDRESS, LSM9DS1_OUT_X_L_XL)
    acc_h = bus.read_byte_data(LSM9DS1_ACC_ADDRESS, LSM9DS1_OUT_X_H_XL)

    acc_combined = (acc_l | acc_h <<8)
    return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readACCy():
    acc_l = bus.read_byte_data(LSM9DS1_ACC_ADDRESS, LSM9DS1_OUT_Y_L_XL)
    acc_h = bus.read_byte_data(LSM9DS1_ACC_ADDRESS, LSM9DS1_OUT_Y_H_XL)

    acc_combined = (acc_l | acc_h <<8)
    return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readACCz():
    acc_l = bus.read_byte_data(LSM9DS1_ACC_ADDRESS, LSM9DS1_OUT_Z_L_XL)
    acc_h = bus.read_byte_data(LSM9DS1_ACC_ADDRESS, LSM9DS1_OUT_Z_H_XL)

    acc_combined = (acc_l | acc_h <<8)
    return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readMAGx():
    mag_l = bus.read_byte_data(LSM9DS1_MAG_ADDRESS, LSM9DS1_OUT_X_L_M)
    mag_h = bus.read_byte_data(LSM9DS1_MAG_ADDRESS, LSM9DS1_OUT_X_H_M)

    mag_combined = (mag_l | mag_h <<8)
    return mag_combined  if mag_combined < 32768 else mag_combined - 65536


def readMAGy():
    mag_l = bus.read_byte_data(LSM9DS1_MAG_ADDRESS, LSM9DS1_OUT_Y_L_M)
    mag_h = bus.read_byte_data(LSM9DS1_MAG_ADDRESS, LSM9DS1_OUT_Y_H_M)

    mag_combined = (mag_l | mag_h <<8)
    return mag_combined  if mag_combined < 32768 else mag_combined - 65536


def readMAGz():
    mag_l = bus.read_byte_data(LSM9DS1_MAG_ADDRESS, LSM9DS1_OUT_Z_L_M)
    mag_h = bus.read_byte_data(LSM9DS1_MAG_ADDRESS, LSM9DS1_OUT_Z_H_M)

    mag_combined = (mag_l | mag_h <<8)
    return mag_combined  if mag_combined < 32768 else mag_combined - 65536



def readGYRx():
    gyr_l = bus.read_byte_data(LSM9DS1_GYR_ADDRESS, LSM9DS1_OUT_X_L_G)
    gyr_h = bus.read_byte_data(LSM9DS1_GYR_ADDRESS, LSM9DS1_OUT_X_H_G)

    gyr_combined = (gyr_l | gyr_h <<8)
    return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536


def readGYRy():
    gyr_l = bus.read_byte_data(LSM9DS1_GYR_ADDRESS, LSM9DS1_OUT_Y_L_G)
    gyr_h = bus.read_byte_data(LSM9DS1_GYR_ADDRESS, LSM9DS1_OUT_Y_H_G)

    gyr_combined = (gyr_l | gyr_h <<8)
    return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536

def readGYRz():
    gyr_l = bus.read_byte_data(LSM9DS1_GYR_ADDRESS, LSM9DS1_OUT_Z_L_G)
    gyr_h = bus.read_byte_data(LSM9DS1_GYR_ADDRESS, LSM9DS1_OUT_Z_H_G)

    gyr_combined = (gyr_l | gyr_h <<8)
    return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536




def initIMU():
                                   #For BerryIMUv2
        #initialise the gyroscope
        writeGRY(LSM9DS1_CTRL_REG4,0b00111000)      #z, y, x axis enabled for gyro
        writeGRY(LSM9DS1_CTRL_REG1_G,0b10111000)    #Gyro ODR = 476Hz, 2000 dps
        writeGRY(LSM9DS1_ORIENT_CFG_G,0b10111000)   #Swap orientation

        #initialise the accelerometer
        writeACC(LSM9DS1_CTRL_REG5_XL,0b00111000)   #z, y, x axis enabled for accelerometer
        writeACC(LSM9DS1_CTRL_REG6_XL,0b00111000)   #+/- 8g

        #initialise the magnetometer
        writeMAG(LSM9DS1_CTRL_REG1_M, 0b10011100)   #Temp compensation enabled,Low power mode mode,80Hz ODR
        writeMAG(LSM9DS1_CTRL_REG2_M, 0b01000000)   #+/-12gauss
        writeMAG(LSM9DS1_CTRL_REG3_M, 0b00000000)   #continuos update
        writeMAG(LSM9DS1_CTRL_REG4_M, 0b00000000)   #lower power mode for Z axis