import threading as th
import time
import config as cfg
import BerryIMU
import Master

lock = th.Lock()
IMU= BerryIMU.IMUoutput()

def

if __name__ == '__main__':
    lock.acquire()
    t1 = th.Thread(target=master)
    t2 = th.Thread(target=IMU.IMU)
    #t3 = th.Thread(target=print_numbers, args=(5,))
    t1.start()
    t2.start()
    #t3.start()

    t1.join()
    t2.join()
    #t3.join()
