import time
import socket

HOST = '192.168.0.8'
PORT = 11010
MAC = 'b8:27:eb:9f:15:29'


while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.8',11010))
    s.sendall('00')
    data = s.recv(1024)
    if(data == 'accept_H'):
        s.sendall(MAC)
    else:
        s.sendall('error:001')
    print data
    s.close()
    time.sleep(5)

