#!/usr/bin/env python3
#"""Ultra simple sample on how to use the library"""
from apa102_pi.driver import apa102
import time
import config as cfg
from led import all_leds
# Initialize the library and the strip
#strip = apa102.APA102(num_led=60, global_brightness=5, mosi=10, sclk=11, order='rbg')

# Turn off all pixels (sometimes a few light up when the strip gets power)
cfg.strip.clear_strip()
ledclass= all_leds()
# Prepare a few individual pixels
#strip.set_pixel_rgb(0, 0xFF0000)  # Red
#strip.set_pixel_rgb(59, 0xFFFFFF)  # White
#strip.set_pixel_rgb(1, 0x00FF00)  # Green

ledclass.set_pixels(0x00FF00)
# Copy the buffer to the Strip (i.e. show the prepared pixels)
cfg.strip.show()

# Wait a few Seconds, to check the result
time.sleep(5)

# Clear the strip and shut down
cfg.strip.clear_strip()
cfg.strip.cleanup()
print ("end")