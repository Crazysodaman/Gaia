import time
import os
import sys
import RPi.GPIO as GPIO

from apa102_pi.driver import apa102
from apa102_pi.colorschemes import colorschemes

def setup():
  # on off comands

  dstart=1 #start daignostics
  etest=1     #eletronics test 1=on 0=off
  servotest=1   #servo test 1=on 0=off
  emo_on=0 #emotions on

  # led set up
  # These two variables should be adjusted to reflect the number of LEDs you have
  # and how bright you want them.
  llevel= 5 #light level for led
  strip= apa102.APA102(num_led=60, global_brightness=llevel, mosi=10, sclk=11, order='rgb')
  time.sleep(0.2)

  ##GPIO PINS and what they are
  #CRelay= 23
  #SDA=2
  #SCL=3

  #Varables


  lt= time.strftime("%A, %B, %Y, %H %M") #local time
  lts= time.strftime("%H %M") #lt short
  cbatt= Cbatt 
  mbatt= Mbatt
  Cbatt= 100 #computer battery %
  Mbatt= 100 #moter battery %
  charging=0
  emos=0 #emotion state
  #IMU varables
  KX=kX #X Kfilter output
  KY=kX #Y Kfilter output
  kX=0
  kY=0

