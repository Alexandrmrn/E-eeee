import socket

clntsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clntsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



clntsock.connect(('localhost', 8080))
while True:
        out = input('Mess: ')
        b_out = out.encode('utf-8')
        clntsock.send(b_out)
        in_data = clientConnection.recv(1024)
        msg = in_data.decode()
        print("From Client :", msg)


