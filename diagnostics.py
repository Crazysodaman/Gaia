import time
import led
import data
import Move

ledtest = 0
servotest = 0
testservos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23, 24)  # All servos see data for servo break down
IMUtest = 0
BMPtest = 0
ssc = data.SSC32()
mve = Move.Move()


def ledtest_change(data):
    global ledtest
    ledtest = data


def ledtest_send():
    return ledtest


def servotest_change(data):
    global servotest
    servotest = data


def servotest_send():
    return servotest


def IMUtest_change(data):
    global IMUtest
    IMUtest = data


def IMUtest_send():
    return IMUtest


def BMPtest_change(data):
    global BMPtest
    BMPtest = data


def BMPtest_send():
    return BMPtest


def testled():
    if ledtest_send() == 1:
        with open('diagnostics.txt', "a") as da:
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Led Test Start \n")
            led.set_red_pixels()
            led.strip.show()
            time.sleep(5)
            led.strip.clear_strip()
            time.sleep(1)
            led.set_blue_pixels()
            led.strip.show()
            time.sleep(5)
            led.strip.clear_strip()
            time.sleep(1)
            led.set_green_pixels()
            led.strip.show()
            time.sleep(5)
            led.strip.clear_strip()
            time.sleep(1)
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Led Test End \n")


def servo_test():
    hia=1250
    hib= 1750
    if servotest_send() == 1:
        with open('diagnostics.txt', "a") as da:
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Servo Test Start \n")
            da.write("Servos that did not go to position:")
            time.sleep(1)
            da.write(mve.testservos(mve.gbf, hia,hib) + ", ")
            time.sleep(1)
            mve.stand(1)
            da.write(mve.testservos(mve.gaf, hib, hia) + ", ")
            time.sleep(1)
            mve.stand(1)
            time.sleep(1)
            da.write(mve.testservos(mve.gbt, hia, hib) + ", ")
            time.sleep(1)
            da.write(mve.testservos(mve.gbr, hia, hib) + ", ")
            time.sleep(1)
            mve.stand(1)
            time.sleep(1)
            da.write(mve.testservos(mve.gat, hib, hia) + ", ")
            time.sleep(1)
            da.write(mve.testservos(mve.gar, hib, hia) + "...")
            time.sleep(1)
            mve.stand(1)
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Servo Test End \n")


def testIMU():
    if IMUtest_send() == 1:
        # TODO work on IMU test
        pass


def testBMP():
    if BMPtest_send() == 1:
        with open('diagnostics.txt', "a") as da:
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "BMP Test Start \n")
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Temp: ")
            da.writelines(str(+ data.tempsend()) + "\n")
            time.sleep(0.5)
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Pressure: ")
            da.writelines(str(+ data.pressend()) + "\n")
            time.sleep(0.5)
            da.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "BMP Test End \n")


if __name__ == '__main__':
    di = open('diagnostics.txt', "a")
    di.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Starting Diagnostics \n")
    di.close()
    ledtest_change(1)  # 1 ON 0 OFF for led test
    testled()
    time.sleep(1)
    servotest_change(1)  # 1 ON 0 OFF for servo test
    servo_test()
    time.sleep(1)
    IMUtest_change(1)  # 1 ON 0 OFF for IMU test
    testIMU()
    time.sleep(1)
    BMPtest_change(1)  # 1 ON 0 OFF for BMP test
    testBMP()
    time.sleep(1)
    di = open('diagnostics.txt', "a")
    di.write(time.strftime("%m/%d/%Y %H:%M:%S: ") + "Ending Diagnostics \n")
    di.close()
