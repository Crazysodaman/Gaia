import runpy
import time
from subprocess import call
import threading as th
import led
import filehandler as fh
import BerryIMU
import GaiaB

EM = 0


def EM_read(data):
    global EM
    EM = data


def EM_show():
    return EM


# TODO Build a file checker for the EM varable


def Main():
    pass
    # lock.acquire()
    # t1 = th.Thread(target=runpy.run_module(GaiaB))
    # t2 = th.Thread(target=runpy.run_module(BerryIMU))  #
    # t3 = th.Thread(target=Errors.Erun)  #
    # t4 = th.Thread(target=timechecker.timechecker)  #
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

    # t1.join()
    # t2.join()
    # t3.join()


if __name__ == '__main__':
    led.strip.clear_strip()
    time.sleep(0.01)
    EM_read(fh.readdataa("Start", "mode"))
    time.sleep(0.01)
    mf = open('log.txt', "a")
    time.sleep(0.5)
    mf.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Starting Up Gaia in mode: ")

    if EM_show() == -1:
        mf.write("OS start \n")  # OS starts and Gaia does not
        mf.close()
        time.sleep(0.5)
        fh.writedataa(0, "Start", "mode")

    elif EM_show() == 0:
        mf.write("Normal\n")
        time.sleep(0.5)
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
        fh.writedataa(-1, "Start", "mode")
        time.sleep(0.5)
        call("sudo shutdown -h now", shell=True)

    elif EM_show() == 2:
        mf.write("Diagnostics\n")
        mf.close()
        led.erleds_change(1)
        led.error_leds()
        runpy.run_module('diagnostics')
        time.sleep(5)
        led.erleds_change(0)
        time.sleep(0.5)
        fh.writedataa(-1, "Start", "mode")
        time.sleep(0.5)
        call("sudo reboot -h now", shell=True)

    else:
        fh.writedataa(-1, "Start", "mode")
        time.sleep(0.5)
        call("sudo reboot -h now", shell=True)
