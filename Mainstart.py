import runpy
import time
import json
from subprocess import call
import threading as th
import led

EM = 0


def EM_read(data):
    global EM
    EM = data


def EM_show():
    return EM

# TODO Build a file checker for the EM varable


def Main():
    # lock.acquire()
    # t1 = th.Thread(target=Master)
    t2 = th.Thread(target=BerryIMU.py)  #
    # t3 = th.Thread(target=Errors.Erun)  #
    # t4 = th.Thread(target=timechecker.timechecker)  #
    # t1.start()
    t2.start()
    # t3.start()
    # t4.start()

    # t1.join()
    t2.join()
    # t3.join()


if __name__ == '__main__':
    led.strip.clear_strip()
    time.sleep(0.01)
    with open("data.json", "r") as start:
        jstart = json.load(start)
        EM_read(jstart["Start"]["mode"])
    time.sleep(0.01)
    mf = open('log.txt', "a")
    mf.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Starting Up Gaia in mode: ")

    if EM_show() == -1:
        mf.write("OS start \n")  # OS starts and Gaia does not
        mf.close()
        with open('start.txt', "w") as start:
            start.write(str(0))

    elif EM_show() == 0:
        mf.write("Normal\n")
        mf.close()

    elif EM_show() == 1:
        mf.write("Safe\n")
        mf.close()
        led.erleds_change(1)
        # t1 = th.Thread(target=led.critical_error_blink())  #
        # t1.start()
        print("running")
        led.erleds_change(0)
        # t1.join(10)
        time.sleep(0.5)
        with open('start.txt', "w") as start:
            start.write(str(-1))
        # call("sudo shutdown -h now", shell=True)

    elif EM_show() == 2:
        mf.write("Diagnostics\n")
        mf.close()
        led.erleds_change(1)
        led.error_leds()
        runpy.run_module('diagnostics')
        time.sleep(5)
        led.erleds_change(0)
        time.sleep(0.5)
        with open('start.txt', "w") as start:
            start.write(str(-1))
        # call("sudo restart -h now", shell=True)
