# This is the master start program

import runpy
import time

import config as cfg
from led import all_leds

ledclass = all_leds()

cfg.strip.clear_strip()

# start main program
# if __name__ == '__main__' :
# os.popen('espeak -p70 -g10 -ven+f3 "Hello I am Gaia" --stdout |aplay')
# time.sleep (3)

# diagnostic start
if cfg.dstart == 1:
    runpy.run_module('daignostics')
    time.sleep(3)

if cfg.EN == 0 and cfg.run_mode == 1:
    runpy.run_module('mp')
    # break

if cfg.EN > 0 and cfg.EN != 3 and cfg.run_mode == 1:
    runpy.run_module('daignostics')
    time.sleep(3)
    input("Continue? Y N")
    cfg.EN = 0

if cfg.EN == 3:  # fatal error handler
    pass
if cfg.EN == -1:  # reset
    pass
