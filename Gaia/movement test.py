import time
import config as cfg
import ssc32 as s32
from led import all_leds

ledclass= all_leds()

cfg.strip

ledclass.set_pixels(0x600080)
cfg.strip.show()
time.sleep (2)
s32.default ()
time.sleep (3)
s32.hightHB ()
#s32.forwardA (5)
time.sleep (3)
s32.default()
cfg.strip.clear_strip()