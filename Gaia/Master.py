## This is the master program for

##import section for varous liberays and other tools

import time
import sys
import socket
import select
import math
import random
import os
import threading as th
from led import all_leds
import runpy
import serial;
import config as cfg #vars

## abbvations for coding perpisous
ledclass= all_leds()

cfg.strip
cfg.strip.clear_strip ()
kalmanX=1
##start of code

#start main program
#if __name__ == '__main__' :
    #os.popen('espeak -p70 -g10 -ven+f3 "Hello I am Gaia" --stdout |aplay')
    #time.sleep (3)
    
    ## diagnostic start
if cfg.dstart ==1:
    runpy.run_module ('daignostics')
    time.sleep (3)

if cfg.EN==0 and cfg.run_mode==1:
runpy.run_module ('mp')

print (cfg.kalmanY)
