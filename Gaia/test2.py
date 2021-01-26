import time
import math
import smbus

import sys
sys.path.insert(0,'/home/pi/Gaia/IMU')
import bmp388

I2C_ADD_BMP388_AD0_LOW = 0x76
I2C_ADD_BMP388_AD0_HIGH = 0x77
I2C_ADD_BMP388 = I2C_ADD_BMP388_AD0_HIGH

def __init__(self, address=I2C_ADD_BMP388):
        self._address = address
        self._bus = smbus.SMBus(0x01)

bmp388.BMP388.get_temperature_and_pressure_and_altitude
print(' Temperature = %.1f Pressure = %.2f  Altitude =%.2f '%(bmp388.temperature/100.0,bmp388.pressure/100.0,bmp388.altitude/100.0))
