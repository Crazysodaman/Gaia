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

    def set_Critical_Error_pixels(self,):#for color it is Hex and 0x to the start of the color
for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0xFF0000, 20)

def set_low_motor_bat(self):
led_num_list[57,58,0,1,2,13,14,15,16,17,28,29,30,31,32,43,44,45,46,47]
for led_number in led_num_list:
strip.set_pixel_rgb(led_number, 0xFF0000)
            
    def set_pixels(self, color):#for color it is Hex and 0x to the start of the color)
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, color)
            
for led_number in range(60):        
