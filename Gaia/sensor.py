import serial;
import time
import config as cfg

uno = serial.Serial("/dev/ttyUSB1", 115200, timeout=0);
uno.open
uno.close