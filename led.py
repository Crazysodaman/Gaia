from apa102_pi.driver import apa102
from apa102_pi.colorschemes import colorschemes
import RPi.GPIO as GPIO
import threading as th
import time
import Mainstart as ms

erleds = 0


def erleds_change(data):
    global erleds
    erleds = data


def erleds_send():
    return erleds


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


def critical_error_blink():
    while erleds_send() == 1:
        set_Critical_Error_pixels()
        strip.show()
        time.sleep(0.25)
        strip.clear_strip()
        time.sleep(0.25)
        erleds_send()
    strip.clear_strip()


def error_leds():
    t1 = th.Thread(target=critical_error_blink())  #
    t1.start()
    t1.join()


def set_low_motor_bat(brightness=20):
    led_num_list = [57, 58, 0, 1, 2, 13, 14, 15, 16, 17, 28, 29, 30, 31, 32, 43, 44, 45, 46, 47]
    for led_number in led_num_list:
        strip.set_pixel_rgb(led_number, 0xFF0000, brightness)


def set_pixels(color, brightness=10):  # for color it is Hex and 0x to the start of the color)
    for led_number in range(60):
        strip.set_pixel_rgb(led_number, color, brightness)


class Color:
    RED = 0xFF0000
    GREEN = 0x00FF00
    BLUE = 0x0000FF
    PURPLE = 0x0F000F


if __name__ == '__main__':
    import time

    set_pixels(0x0D001A, 20)
    strip.show()
    time.sleep(1)
    strip.clear_strip()
    time.sleep(1)
    set_pixels(0x0F000F, 20)
    strip.show()
    time.sleep(1)
    strip.clear_strip()
    time.sleep(1)
    error_leds()
