import time
import os
import sys
import concurrent.futures
import subprocess
import bmp388 as bmp

from apa102_pi.driver import apa102
from apa102_pi.colorschemes import colorschemes

# on off comands

dstart=1 #start daignostics
etest=1     #eletronics test 1=on 0=off
servotest=1   #servo test 1=on 0=off
emo_on=0 #emotions on

# led set up
# These two variables should be adjusted to reflect the number of LEDs you have
# and how bright you want them.
llevel=5 #light level for led
strip= apa102.APA102(num_led=60, global_brightness=llevel, mosi=10, sclk=11, order='rgb')
time.sleep(0.2)

#Varables

lt= time.strftime("%A, %B, %Y, %H %M") #local time
lts= time.strftime("%H %M") #lt short
Cbatt= 100 #computer battery %
Mbatt= 100 #moter battery %
cbatt= Cbatt 
mbatt= Mbatt
emos=0 #emotion state
#IMU varables
kX=0
kY=0
KX=kX #X Kfilter output
KY=kX #Y Kfilter output
