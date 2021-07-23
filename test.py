

#ef leg (S1,P1,S2,S3,P2,P3,ms):
    #ssc.write (f"#{S1} P{P1} #{S2} P{P2} #{S3} P{P3} T{ms} \r".encode()) #leg

leg(2,3,5,1500,1400,900,100)
time
leg()
time
leg()

def leg (ms, *args):

    command = ""
    for servo in args:
        command += f"#{servo[0]} P{servo[1]} "
    command += f"T{ms} \r"
    ssc.write (command.encode()) #leg

leg(100,(1,2000),(3,1500))
a=((3,1200),(5,750))
def leg(ms: int, *args: tuple) -> None: