import threading as th
import time
import config as cfg
import BerryIMU
import Master
import timechecker
import Errors

lock = th.Lock()
IMU= BerryIMU.IMUoutput()

if __name__ == '__main__':
    #lock.acquire()
    #t1 = th.Thread(target=Master)
    t2 = th.Thread(target=IMU.IMU)
    t3 = th.Thread(target=Errors.Erun)
    t4 = th.Thread(target=timechecker.timechecker)
    #t1.start()
    t2.start()
    t3.start()
    t4.start()

    #t1.join()
    #t2.join()
    #t3.join()
    time.sleep(1.5)
    print(cfg.tiltCompensatedHeading)