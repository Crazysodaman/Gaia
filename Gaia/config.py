import time
import os
import sys
import RPi.GPIO as GPIO
from multiprocessing import Process, Pipe
from apa102_pi.driver import apa102
from apa102_pi.colorschemes import colorschemes

# on off comands

dstart=0 #start daignostics
etest=0     #eletronics test 1=on 0=off
servotest=0   #servo test 1=on 0=off
IMU=1 #IMU on off
emo_on=0 #emotions on
run_mode=1 #run
EN=3 #error number
# led set up
# These two variables should be adjusted to reflect the number of LEDs you have
# and how bright you want them.

strip = apa102.APA102(num_led=60, mosi=10, sclk=11, order='rgb')

##GPIO PINS and what they are
#CRelay= 23
#SDA=2
#SCL=3

#Varables

def tm (tg=3):
    if tg == 1:
        return time.strftime("%A, %B, %d, %Y, %H %M")
    if tg == 2:
        return time.strftime("%B, %d, %Y\n ")#local time file
    if tg == 3:
        return time.strftime("%H %M")
    if tg == 4:
        return time.strftime("%H:%M:%S \n")#lt short file

Cbatt= 100 #computer battery %
Mbatt= 100 #moter battery %
cbatt= Cbatt 
mbatt= Mbatt

charging=0
emos=0 #emotion state


#IMU varables
kalmanX =0
kalmanY =0
tiltCompensatedHeading =0
ACCx=0
ACCy=0
ACCz=0
gyroXangle=0
gyroYangle=0
gyroZangle=0


