import time
import RPi.GPIO as GPIO
import config as cfg
import ssc32 as s32


CRelay= 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #set pins to GPIO# like GPIO 4 is #7 on board
GPIO.setup(CRelay, GPIO.OUT)
GPIO.output(CRelay, GPIO.LOW)

def relayon()
  if
    GPIO.output(CRelay, GPIO.HIGH)
    #if (insert voltage here) >= 100%
    GPIO.output(CRelay, GPIO.LOW))
