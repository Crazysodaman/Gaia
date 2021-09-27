import threading as th
import time

import Errors
import config as cfg
import timechecker
from Gaia import BerryIMU

lock = th.Lock()
IMU = BerryIMU.IMUoutput()

if __name__ == '__main__':
    # lock.acquire()
    # t1 = th.Thread(target=Master)
    t2 = th.Thread(target=IMU.IMU)  #
    t3 = th.Thread(target=Errors.Erun)  #
    t4 = th.Thread(target=timechecker.timechecker)  #
    # t1.start()
    t2.start()
    t3.start()
    t4.start()
    while True:
        # t1.is_alive()
        t = [t2.is_alive(), t3.is_alive(), t4.is_alive()]

        if not all(t):
            cfg.EN = 1

            break

    if cfg.EN > 0:
        # t1.join()
        t2.join()
        t3.join()
    time.sleep(1.5)
    print(cfg.tiltCompensatedHeading)
