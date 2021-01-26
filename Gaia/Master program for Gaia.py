## This is the master program for

##import section for varous liberays and other tools

import time
import sys
import socket
import select
import math
import random
import os
from led import all_leds
import serial;
import runpy
import config as cfg #vars
import RPi.GPIO as GPIO

## abbvations for coding perpisous
ledclass= all_leds()

##GPIO PINS and what they are
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #set pins to GPIO# like GPIO 4 is #7 on board

cfg.strip
cfg.strip.clear_strip ()

##start of code
def ultimate_function():
    os.popen('espeak -p70 -g10 -ven+f3 "Hello I am Gaia" --stdout |aplay')
    time.sleep (3)
    ## diagnostic start

    if cfg.dstart ==1:
        runpy.run_module ('daignostics')
        time.sleep (3)

#start main program
   
