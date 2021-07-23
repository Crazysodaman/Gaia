import data


def send_gaia():
    pass


def receive_gaia():
    pass


def receive_data(var):
    """
    :param var:1-Cbatt, 2-Mbatt,
    """
    if var == 1:
        return data.send_cbatt()
    elif var == 2:
        return data.send_mbatt()
