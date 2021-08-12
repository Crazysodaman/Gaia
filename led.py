from apa102_pi.driver import apa102
from apa102_pi.colorschemes import colorschemes
import RPi.GPIO as GPIO

# usage:
# all_leds = all_leds() #it will use the default 61 numbers, = all_leds(610) will use 610 leds
# all_leds.set_red_pixels() # will set to red
# all_leds.set_blue_pixels() # will set to blue
strip = apa102.APA102(num_led=60, mosi=10, sclk=11, order='rgb')


def set_red_pixels():
    for led_number in range(60):
        strip.set_pixel_rgb(led_number, 0xFF0000)

def set_green_pixels():
    for led_number in range(60):
        strip.set_pixel_rgb(led_number, 0x00FF00)

def set_blue_pixels():
    for led_number in range(60):
        strip.set_pixel_rgb(led_number, 0x0000FF)

def set_Critical_Error_pixels(brightness=20):  # for color it is Hex and 0x to the start of the color
    for led_number in range(60):
        strip.set_pixel_rgb(led_number, 0xFF0000, brightness)
        while True:
            strip.show()
            time.sleep(0.5)
            strip.clear_strip()
            if EM<=0
            break

def set_low_motor_bat(brightness=20):
    led_num_list = [57, 58, 0, 1, 2, 13, 14, 15, 16, 17, 28, 29, 30, 31, 32, 43, 44, 45, 46, 47]
    for led_number in led_num_list:
        strip.set_pixel_rgb(led_number, 0xFF0000, brightness)

def set_pixels(color, brightness=10):  # for color it is Hex and 0x to the start of the color)
    for led_number in range(60):
        strip.set_pixel_rgb(led_number, color, brightness)

if __name__ == '__main__':
    import time
    set_pixels(0x0D001A,20)
    strip.show()
    time.sleep(1)
    strip.clear_strip()