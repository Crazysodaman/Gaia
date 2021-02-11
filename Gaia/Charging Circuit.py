import time
import RPi.GPIO as GPIO
import ssc32 as s32


CRelay= 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #set pins to GPIO# like GPIO 4 is #7 on board
GPIO.setup(CRelay, GPIO.OUT)
GPIO.output(CRelay, GPIO.LOW)

if cfg.charging == 1
  s32.32cl
  GPIO.output(CRelay, GPIO.HIGH)
