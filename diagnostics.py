import time
import led
import data

ledtest = 0
servotest = 0
testservos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23, 24)  # All servos see data for servo break down
IMUtest = 0
BMPtest = 0


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


def servo_test():
    if servotest_send() == 1:
        print(data.sendservopos(testservos))
        time.sleep(1)
        data.servomove(100, (0, 1500), (1, 1500), (2, 1500), (3, 1500), (4, 1500), (5, 1500), (6, 1500), (7, 1500),
                       (8, 1500), (16, 1500), (17, 1500), (18, 1500), (19, 1500), (20, 1500), (21, 1500), (22, 1500),
                       (23, 1500), (24, 1500))
        time.sleep(1)
        print(data.sendservopos(testservos))
        time.sleep(1)
        data.servomove(100, (0, 900), (1, 900), (2, 900), (3, 1500), (4, 1500), (5, 1500), (6, 900), (7, 900), (8, 900),
                       (16, 1500),
                       (17, 1500), (18, 1500), (19, 2000), (20, 2000), (21, 2000), (22, 1500),
                       (23, 1500), (24, 1500))  # moving 0,1,2,6,7,8,19,20,21
        time.sleep(1)
        print(data.sendservopos(testservos))
        time.sleep(1)
        data.servomove(100, (0, 1500), (1, 1500), (2, 1500), (3, 1500), (4, 1500), (5, 1500), (6, 1500), (7, 1500),
                       (8, 1500), (16, 1500), (17, 1500), (18, 1500), (19, 1500), (20, 1500), (21, 1500), (22, 1500),
                       (23, 1500), (24, 1500))
        time.sleep(1)
        print(data.sendservopos(testservos))
        time.sleep(1)
        data.servomove(100, (0, 1500), (1, 1500), (2, 1500), (3, 900), (4, 900), (5, 900), (6, 1500), (7, 1500),
                       (8, 1500), (16, 1500), (17, 1500), (18, 1500), (19, 1500), (20, 1500), (21, 1500), (22, 1500),
                       (23, 1500), (24, 1500))  # moving 3,4,5,16,17,18,22,23,24
        time.sleep(1)
        print(data.sendservopos(testservos))
        time.sleep(1)
        data.servomove(100, (0, 1500), (1, 1500), (2, 1500), (3, 1500), (4, 1500), (5, 1500), (6, 1500),
                       (7, 1500), (8, 1500), (16, 1500), (17, 1500), (18, 1500), (19, 1500), (20, 1500),
                       (21, 1500), (22, 1500), (23, 1500), (24, 1500))
        time.sleep(1)
        print(data.sendservopos(testservos))
        time.sleep(1)


def testIMU():
    if IMUtest_send() == 1:
        # TODO work on IMU test
        pass


def testBMP():
    if BMPtest_send() == 1:
        print("Temp:" + data.tempsend())
        time.sleep(0.5)
        print("Pressure" + data.pressend())


if __name__ == '__main__':
    ledtest_change(1)  # 1 ON 0 OFF for led test
    testled()
    time.sleep(1)
    servotest_change(1)  # 1 ON 0 OFF for servo test
    servo_test()
    time.sleep(1)
    IMUtest_change(1)
    testIMU()
    time.sleep(1)
    BMPtest_change(1)
    testBMP()
    time.sleep(1)
