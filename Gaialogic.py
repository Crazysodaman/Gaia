import time
import data
import GaiaB as gb


def send_gaia():
    pass


def receive_gaia():
    pass


def receive_batt_data(var):
    """
    :param var:1-Cbatt, 2-Mbatt,
    """
    if var == 1:
        return data.send_cbatt()
    elif var == 2:
        return data.send_mbatt()


def receive_IMU_data(var):
    """
    1-12
    :param var:1-ACCx, 2-ACCy, 3- ACCz, 4-GYRx, 5-GYRy, 6-GYRz, 7-MAGx, 8-MAGy, 9-MAGz, 10-kalmanY, 11-kalmanX, 12-tiltCompensatedHeading
    """
    if var == 1:
        return data.ACCx_send()
    elif var == 2:
        return data.ACCy_send()
    elif var == 3:
        return data.ACCz_send()
    elif var == 4:
        return data.GYRx_send()
    elif var == 5:
        return data.GYRy_send()
    elif var == 6:
        return data.GYRz_send()
    elif var == 7:
        return data.MAGx_send()
    elif var == 8:
        return data.MAGy_send()
    elif var == 9:
        return data.MAGz_send()
    elif var == 10:
        return data.kalmanY_send()
    elif var == 11:
        return data.kalmanX_send()
    elif var == 12:
        return data.tiltCompensatedHeading_send()


def critical_data_send_gaia(var):
    """
    :param var: 1-CBatt low, 2-MBatt low
    """
    if var == 1 and receive_batt_data(1) < 10:
        return
    elif var == 2 and receive_batt_data(2) < 10:
        return
    else:
        pass


def servomove(ms: int, *args: tuple) -> None:
    """
    A = [(1,1500),(2,1500)]
    Exmple: leg(100,(1,1500),(2,1500),(3,1500))
    :param ms: Time it has to move
    :param args: (# (servo), P(position))
    """
    command: str = ""
    for servo in args:
        command += f"#{servo[0]} P{servo[1]} "
    command += f"T{ms} \r"
    with serial.Serial("/dev/ttyUSB0", 115200, timeout=0) as ssc:
        ssc.write(command.encode())


def low_battery():
    mf = open('log.txt', "a")
    if data.send_cbatt() < 10 and data.send_mbatt() < 10:
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Computer Battery Low \n")
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Motor Battery Low \n")
        mf.close()
    elif data.send_cbatt() < 10:
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Computer Battery Low \n")
        mf.close()
    elif data.send_mbatt() < 10:
        mf.write(time.strftime("%m/%d/%Y;%H:%M:%S: ") + "Motor Battery Low \n")
        mf.close()
    print("yes")
    change_needs_charging(1)


def change_needs_charging(data):
    gb.needscharging = data


def send_needs_charging():
    return gb.needscharging


if __name__ == '__main__':
    pass
