## This is the master program for

##import section for varous liberays and other tools

import time
import sys
import socket
import select
import math
import random
from pexecute.thread import ThreadLoom
import os
from led import all_leds
import serial;
import runpy
import config as cfg #vars
import RPi.GPIO as GPIO

## abbvations for coding perpisous
loom= ThreadLoom(max_runner_cap=20)
ledclass= all_leds()
ssc = serial.Serial("/dev/ttyUSB0", 115200, timeout=0);
ssc.open
ssc.close
    ##used to command movements
    ##ssc.close
    ##ssc.write dont forget \r" .encode()

##GPIO PINS and what they are
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #set pins to GPIO# like GPIO 4 is #7 on board

# Some standard colors for the ring.
#strip.set_pixel_rgb(60,  0xFF0000)  ##Red
#strip.set_pixel_rgb(60, 0x00FF00) ##Green
#strip.set_pixel_rgb(60, 0x0000FF)  ##Blue
cfg.strip
cfg.strip.clear_strip ()
##


##start of code
def ultimate_function():
    os.popen('espeak -p70 -g10 -ven+f3 "Hello I am Gaia" --stdout |aplay')
    time.sleep (3)
    ## diagnostic start

    if cfg.dstart ==1:
        runpy.run_module ('daignostics')
        time.sleep (3)    
    #start main program
    os.popen( 'espeak -p70 -g10 -ven+f3 "It is: {}" --stdout |aplay' .format(cfg.lts))
    #insert led normal color
    
def IMU():
    runpy.run_module ('BerryIMU')
loom.add_function(ultimate_function)
loom.add_function(IMU)
output+loom.execute()