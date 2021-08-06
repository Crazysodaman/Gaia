import socket, time

HOST = '78.45.36.46'
PORT = 60001


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        while True:
            client.sendall(b'Hello, Fuck')