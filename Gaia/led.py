import config as cfg
import time
from apa102_pi.driver import apa102
from apa102_pi.colorschemes import colorschemes


#usage:
#all_leds = all_leds() #it will use the default 61 numbers, = all_leds(610) will use 610 leds
#all_leds.set_red_pixels() # will set to red
#all_leds.set_blue_pixels() # will set to blue
   
class all_leds:
    
    def __init__ (self): #number_of_leds here is an optional argument, by default it is 61, but you may set your own number
        
        pass
    def set_red_pixels(self):
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0xFF0000)

    def set_green_pixels(self):
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0x00FF00)

    def set_blue_pixels(self):
        for led_number in range(60):
            strip.set_pixel_rgb(led_number, 0x0000FF)

    def set_Critical_Error_pixels(self,):#for color it is Hex and 0x to the start of the color)
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0xFF0000, 20)

def set_low_motor_bat(self):
cfg.strip.set_pixel_rgb(58, 0xFF0000)#
cfg.strip.set_pixel_rgb(59, 0xFF0000)
cfg.strip.set_pixel_rgb(0, 0xFF0000) #
cfg.strip.set_pixel_rgb(1, 0xFF0000)
cfg.strip.set_pixel_rgb(2, 0xFF0000)#
cfg.strip.set_pixel_rgb(13, 0xFF0000)#
cfg.strip.set_pixel_rgb(14, 0xFF0000)
cfg.strip.set_pixel_rgb(15, 0xFF0000) #
cfg.strip.set_pixel_rgb(16, 0xFF0000)
cfg.strip.set_pixel_rgb(17, 0xFF0000)#
cfg.strip.set_pixel_rgb(28, 0xFF0000)#
cfg.strip.set_pixel_rgb(29, 0xFF0000)
cfg.strip.set_pixel_rgb(30, 0xFF0000)#
cfg.strip.set_pixel_rgb(31, 0xFF0000)
cfg.strip.set_pixel_rgb(32, 0xFF0000)#
cfg.strip.set_pixel_rgb(43, 0xFF0000)#
cfg.strip.set_pixel_rgb(44, 0xFF0000)
cfg.strip.set_pixel_rgb(45, 0xFF0000)#
cfg.strip.set_pixel_rgb(46, 0xFF0000)
cfg.strip.set_pixel_rgb(47, 0xFF0000)#
            
    def set_pixels(self, color):#for color it is Hex and 0x to the start of the color)
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, color)
            
for led_number in range(60):        
