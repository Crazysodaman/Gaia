def servomove(ms: int, servo: list, pos: list) -> None:
    """
    Exmple: leg(100, Servos, Positions (750-2500))
    :param ms: Time it has to move
    :param args: (# (servo), P(position))
    """
    # list(zip(servo,pos))
    command: str = ""
    for long in zip(servo, pos):
        command += f"#{long[0]} P{long[1]} "
    command += f"T{ms} \r"
    print(command)

A=[3,5,7,9]
B=[500,750,2500,1200]
servomove(50,A,B)