import runpy
import time
from subprocess import call
import threading as th
#import led

EM = 0


def EM_change(data):
    global EM
    EM = int(data.strip(''))


def EM_show():
    return EM


if __name__ == '__main__':
    time.sleep(0.01)
    with open('start.txt', "r") as start:
        EM_change(start.read())
    time.sleep(0.01)
    mf = open('log.txt', "a")
    mf.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Starting Up Gaia in mode: ")

    if EM_show() == -1:
        mf.write("OS start \n")  # OS starts and Gaia does not
        mf.close()

    elif EM_show() == 0:
        mf.write("Normal\n")
        mf.close()

    elif EM_show() == 1:
        mf.write("Safe\n")
        mf.close()
        print("running")

        time.sleep(0.5)

        # call("sudo shutdown -h now", shell=True)

    elif EM_show() == 2:
        mf.write("Diagnostics\n")
        mf.close()
        #led.erleds_change(1)
        #runpy.run_module('diagnostics')
        time.sleep(5)
        with open('start.txt', "w") as start:
            start.write(str(-1))
        time.sleep(0.5)
        # call("sudo restart -h now", shell=True)
