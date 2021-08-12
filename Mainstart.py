import time
import led
EM= -1

def Main():
    # lock.acquire()
    # t1 = th.Thread(target=Master)
    t2 = th.Thread(target=Gaia.Gaia.BerryIMU)  #
    #t3 = th.Thread(target=Errors.Erun)  #
    #t4 = th.Thread(target=timechecker.timechecker)  #
    # t1.start()
    t2.start()
    #t3.start()
    #t4.start()

    # t1.join()
    t2.join()
    #t3.join()

if __name__ == '__main__':
    led.strip.clear_strip ()
    time.sleep(0.01)
    mf = open('log.txt', "a")
    mf.write(time.strftime("%m/%d/%Y %H:%M:%S: ")+ "Starting Up Gaia in mode: ")
    if EM== -1:
        mf.write ("OS start \n") #OS starts and Gaia does not
        mf.close()
    elif EM==0:
        mf.write("Normal\n")
        mf.close()
        Main()
    elif EM==1:
        mf.write("Safe\n")
        mf.close()
        led.set_Critical_Error_pixels()
        led.strip.show()
    elif EM==2:
        mf.write("Diagnostics\n")
        mf.close()
        led.set_Critical_Error_pixels()
        led.strip.show()
