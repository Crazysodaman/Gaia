import time
import sys
import socket
import os
import config as cfg
import serial;
from led import all_leds
import led
import ssc32 as s32
import RPi.GPIO as GPIO

#led setup
ledclass= all_leds()

os.popen( 'espeak -p70 -g20 -ven+f3 "Starting diagnostics" --stdout |aplay' )
time.sleep(3)
os.popen( 'espeak -p70 -g20 -ven+f3 "Local Time: {}" --stdout |aplay' .format(cfg.lt))
time.sleep(7)
time.sleep (4)
os.popen( 'espeak -p70 -g20 -ven+f3 "Computer battery {}%" --stdout |aplay' .format(cfg.cbatt))
time.sleep (4)
if cfg.cbatt <=10:
    os.popen( 'espeak -p70 -g20 -ven+f3 "Charge or Replace Computer battery" --stdout |aplay')
    time.sleep (4)
os.popen( 'espeak -p70 -g20 -ven+f3 "Motor battery {}%" --stdout |aplay' .format(cfg.mbatt))
time.sleep (4)
if cfg.mbatt <=10:
    os.popen( 'espeak -p70 -g20 -ven+f3 "Charge or Replace Motor battery" --stdout |aplay')
    time.sleep (4)

if cfg.etest == 1:
    time.sleep (1)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Electronic Test starting" --stdout |aplay' )
    time.sleep (4)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Testing Ring" --stdout |aplay' )
    time.sleep (3)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Red" --stdout |aplay' )
    ledclass.set_red_pixels()
    cfg.strip.show()
    time.sleep (5)
    cfg.strip.clear_strip()
    time.sleep (1)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Blue" --stdout |aplay' )
    ledclass.set_blue_pixels()
    cfg.strip.show()
    time.sleep (5)
    cfg.strip.clear_strip()
    time.sleep (1)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Green" --stdout |aplay' )
    ledclass.set_green_pixels()
    cfg.strip.show()
    time.sleep (5)
    cfg.strip.clear_strip()
    time.sleep (1)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Low Computer battery Light" --stdout |aplay' ) ## leds should be flashing red X
    time.sleep (5)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Low Motor battery Light" --stdout |aplay' )    ##leds shoud be flashing red +
                                                                                        ##if both are on means both batterys are low
    time.sleep (5)
    os.popen( 'espeak -p70 -g20 -ven+f3 "GPS and IMU Test" --stdout |aplay' )
    time.sleep (5)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Kalman X {}" --stdout |aplay' .format(cfg.KX))
    time.sleep (5)
    os.popen( 'espeak -p70 -g20 -ven+f3 "Electronic Test complete" --stdout |aplay' )
    time.sleep (4)

if cfg.testcharge == 1:
time.sleep (2)
Charging.relayon()
if cfg.servotest == 1:
    os.popen( 'espeak -p70 -g20 -ven+f3 "Servo test starting" --stdout |aplay' )
    time.sleep (3)
    s32.default()
    os.popen( 'espeak -p70 -g20 -ven+f3 "Servo test Completed" --stdout |aplay' )
    time.sleep (3)

os.popen( 'espeak -p70 -g20 -ven+f3 "Diagnostics Completed" --stdout |aplay' )
time.sleep (3)
