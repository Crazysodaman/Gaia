import time

import config as cfg


def timechecker():
    t1 = time.strftime("%D")
    t2 = time.strftime("%H")
    while True:
        t3 = time.strftime("%D")
        t4 = time.strftime("%H")
        if t1 != t3:
            e = open('Errors.txt', "a")
            e.writelines(cfg.tm(2))
            e.close()
            cfg.EN = 0
            d = open('Data.txt', "a")
            d.writelines(cfg.tm(2))
            d.close()
        t1 = t3
        if t2 != t4:
            d = open('Data.txt', "a")
            d.writelines(cfg.tm(4))
            d.close()
            time.sleep(3600)
        t2 = t4
        if cfg.EN > 0:
            break


if __name__ == '__main__':
    timechecker()
