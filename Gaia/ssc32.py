import serial
import time

ssc = serial.Serial("/dev/ttyUSB0", 115200, timeout=0);
ssc.open
ssc.close


# used to command movements
# ssc.close
# ssc.write dont forget \r" .encode()
# servo and numbers
# FRR-8   FLR-24
# FRT-7   FLT-23
# FRFT-6  FLFT-22
# CRR-5   CLR-21
# CRT-4   CLT-20
# CRFT-3  CLFT-19
# BRR-2   BLR-18
# BRT-1   BLT-17
# BRFT-0  BLFT-16

# leg groups
# A
# (8,7,6),(21,20,19),(2,1,0)
# B
# (24,23,22),(5,4,3),(18,17,16 )

def default():
    """
    Sets legs to default
    """
    ssc.open
    ssc.write("#0 P1500 #1 P1500 #2 P1500 T100 \r".encode())
    ssc.write("#3 P1500 #4 P1500 #5 P1500 T100 \r".encode())
    ssc.write("#6 P1500 #7 P1500 #8 P1500 T100 \r".encode())
    ssc.write("#16 P1500 #17 P1500 #18 P1500 T100 \r".encode())
    ssc.write("#19 P1500 #20 P1500 #21 P1500 T100 \r".encode())
    ssc.write("#22 P1500 #23 P1500 #24 P1500 T100 \r".encode())
    time.sleep(2)
    ssc.close


def leg(ms: int, *args: tuple) -> None:
    """
    Exmple: leg(100,(1,1500),(2,1500),(3,1500))
    :param ms: Time it has to move
    :param args: (# (servo), P(position))
    """
    command: str = ""
    for servo in args:
        command += f"#{servo[0]} P{servo[1]} "
    command += f"T{ms} \r"
    ssc.write(command.encode())


def hightHA(ms):
    ssc.open
    ssc.write(f"#0 P1700 #3 P1700 #6 P1700 T{ms} \r".encode())  # R legs
    ssc.write(f"#1 P1700 #4 P1700 #7 P1700 T{ms} \r".encode())  # R thighs
    ssc.write(f"#16 P1300 #19 P1300 #22 P1300 T{ms} \r".encode())  # L legs
    ssc.write(f"#17 P1300 #20 P1300 #23 P1300 T{ms} \r".encode())  # L Thighs
    ssc.close


def forwardA(tt, ms):
    ts = 0.3
    t_end = time.time() + tt
    while time.time() < t_end:  # or snr.ldr1 <10:
        ssc.open
        ssc.write(f"#7 P1250 #20 P1750 #1 P1250 T{ms} \r".encode())  # a up
        time.sleep(ts)
        ssc.write(f"#8 P900 #21 P2100 #2 P900 T{ms} \r".encode())  # a move
        time.sleep(ts)
        ssc.write(f"#7 P1500 #20 P1500 #1 P1500 T{ms} \r".encode())  # a down
        time.sleep(ts)
        ssc.write(f"#23 P1750 #4 P1250 #17 P1750 T{ms} \r".encode())  # b up
        time.sleep(ts)
        ssc.write(f"#8 P1500 #21 P1500 #2 P1500 T{ms} \r".encode())  # a move
        time.sleep(ts)
        ssc.write(f"#24 P2100 #5 P900 #18 P2100 T{ms} \r".encode())  # b move
        time.sleep(ts)
        ssc.write(f"#23 P1500 #4 P1500 #17 P1500 T{ms} \r".encode())  # b down
        time.sleep(ts)
        ssc.write(f"#7 P1250 #20 P1750 #1 P1250 T{ms} \r".encode())  # a up
        time.sleep(ts)
        ssc.write(f"#24 P1500 #5 P1500 #18 P1500 T{ms} \r".encode())  # b move
        time.sleep(ts)
    ssc.write(
        "#0 P1500 #1 P1500 #2 P1500 #3 P1500 #4 P1500 #5 P1500 #6 P1500 #7 P1500 #8 P1500 #16 P1500 #17 P1500 #18 P1500 #19 P1500 #20 P1500 #21 P1500 #22 P1500 #23 P1500 #24 P1500 T100 \r".encode())
    ssc.close


def backwardA(tt, ms):
    ts = 0.3
    t_end = time.time() + tt
    while time.time() < t_end:  # or snr.ldr1 <10:
        ssc.open
        ssc.write(f"#7 P1100 #20 P1900 #1 P900 T{ms} \r".encode())  # a up
        time.sleep(ts)
        ssc.write(f"#8 P1900 #21 P1100 #2 P1900 T{ms} \r".encode())  # a move
        time.sleep(ts)
        ssc.write(f"#7 P1500 #20 P1500 #1 P1500 T{ms} \r".encode())  # a down
        time.sleep(ts)
        ssc.write(f"#23 P1900 #4 P900 #17 P1900 T{ms} \r".encode())  # b up
        time.sleep(ts)
        ssc.write(f"#8 P1500 #21 P1500 #2 P1500 T{ms} \r".encode())  # a move
        time.sleep(ts)
        ssc.write(f"#24 P1100 #5 P1900 #18 P1100 T{ms} \r".encode())  # b move
        time.sleep(ts)
        ssc.write(f"#23 P1500 #4 P1500 #17 P1500 T{ms} \r".encode())  # b down
        time.sleep(ts)
        ssc.write(f"#7 P1100 #20 P1900 #1 P900 T{ms} \r".encode())  # a up
        time.sleep(ts)
        ssc.write(f"#24 P1500 #5 P1500 #18 P1500 T{ms} \r".encode())  # b move
        time.sleep(ts)
    ssc.write(
        "#0 P1500 #1 P1500 #2 P1500 #3 P1500 #4 P1500 #5 P1500 #6 P1500 #7 P1500 #8 P1500 #16 P1500 #17 P1500 #18 P1500 #19 P1500 #20 P1500 #21 P1500 #22 P1500 #23 P1500 #24 P1500 T100 \r".encode())
    ssc.close


def death1(ft):
    t_end = time.time() + ft
    while time.time() < t_end:  # or snr.ldr1 <10:
        ssc.open
        ssc.write("#7 P1500 #6 P1500 #20 P1500 #19 P1500 #1 P1500 #0 P1500 T2500 \r".encode())
        time.sleep(0.2)
        ssc.write("#8 P1500 #21 P1500 #2 P1500 T2500 \r".encode())
        time.sleep(0.2)
        ssc.write("#7 P100 #6 P100 #20 P100 #19 P100 #1 P100 #0 P100 T2500 \r".encode())
        time.sleep(0.2)
        ssc.write("#23 P1500 #22 P1500 #4 P1500 #3 P1500 #17 P1500 #16 P1500 T2500 \r".encode())
        time.sleep(0.2)
        ssc.write("#24 P500 #5 P500 #18 P500 T2500 \r".encode())
        time.sleep(0.2)
        ssc.write("#23 P500 #22 P500 #4 P500 #3 P500 #17 P500 #16 P500 T2500 \r".encode())
        ssc.close


def servotest():
    ssc.open
    ssc.write("#0 P1500 #6 P1500 #20 P1500 #19 P1500 #1 P1500 #0 P1500 T2500 \r".encode())
    time.sleep(0.2)
    ssc.write("#8 P1500 #21 P1500 #2 P1500 T2500 \r".encode())
    time.sleep(0.2)
    ssc.write("#7 P100 #6 P100 #20 P100 #19 P100 #1 P100 #0 P100 T2500 \r".encode())
    time.sleep(0.2)
    ssc.write("#23 P1500 #22 P1500 #4 P1500 #3 P1500 #17 P1500 #16 P1500 T2500 \r".encode())
    time.sleep(0.2)
    ssc.write("#24 P500 #5 P500 #18 P500 T2500 \r".encode())
    time.sleep(0.2)
    ssc.close


leg()
