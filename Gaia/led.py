import config as cfg
#usage:

#cfg.strip.set_pixel_rgb(lednumber, color)
#all_leds = all_leds() #it will use the default 60 numbers, = all_leds(60) will use 60 leds
#all_leds.set_red_pixels() # will set to red
#all_leds.set_blue_pixels() # will set to blue
   
class all_leds:
    
    def __init__ (self): #number_of_leds here is an optional argument, by default it is 60, but you may set your own number
        
        pass

    def set_red_pixels(self):
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0xFF0000)

    def set_green_pixels(self):
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0x00FF00)

    def set_blue_pixels(self):
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, 0x0000FF)
            
    def set_pixels(self, color):
        for led_number in range(60):
            cfg.strip.set_pixel_rgb(led_number, color)
            
#
