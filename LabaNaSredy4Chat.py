import socket
import time


sock = socket.socket()
sock.bind(("127.0.0.1",8080))
sock.listen(1)
print('Ожидание подключения..')
conn, adr = sock.accept()
print('Подключен'+str(adr))
text = 'Отправьте матрицу'
conn.send(text.encode())
text = conn.recv(65565).decode()
if str(text) == "time":
    text = time.strftime("Today is %B %d, %Y.", time.localtime())
    conn.send(text.encode())


