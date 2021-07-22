import time
import config as cfg
import led
from led import all_leds
led=all_leds()
def Erun():
    while True:
        if cfg.EN==-1:
            e = open('Errors.txt', "w")
            e.writelines(cfg.tm(2) )
            e.close()
            cfg.EN = 0
        if cfg.EN==1:
            e=open('Errors.txt', "a")
            e.writelines(cfg.tm(4))
            e.write('Johnny is fat \n')
            e.close()
            cfg.EN=0
        if cfg.EN==2:
            e = open('Errors.txt', "a")
            e.writelines(cfg.tm(4))
            e.write('Johnny is love \n')
            e.close()
            cfg.EN=0
        if cfg.EN == 3:
            e = open('Errors.txt', "a")
            e.writelines(cfg.tm(4))
            e.write('Johnny is hungery \n')
            e.close()
            cfg.run_mode=0

break

if cfg.EN ==3:
while True:
cfg.strip.clear_strip()
led.set_Critical_Error_pixels()
cfg.strip.show()
time.sleep(1)
cfg.strip.clear_strip()
time.sleep(1)
        
            
            
                


if __name__ == '__main__':
    Erun()
