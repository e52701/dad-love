import os
import shutil
import socket
import datetime

#block of file option
path = os.getcwd() + '/data'#the path of saved file
H_path = path + '/HeartBeat.txt'#heart file name
D_path = path + '/Data.txt'#data file name

#blcok of socket option
HOST = '192.168.0.8'#server IP
PORT = 11010#server port
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create socket net
s.bind((HOST,PORT))#bind server
s.listen(50)#the number of link

#block of led light
light = ['100000000','000100000','000000100']

#create file and delete file.
def create_file():
    delete_file()
    os.mknod(path + '/Data.txt')
    os.mknod(path + '/HeartBeat.txt')
    print 'create success'
    return

def delete_file():
    os.remove(path + '/HeartBeat.txt')
    os.remove(path + '/Data.txt')
    print 'delete success'
    return

#add HeartBeat data
def add_Heart(H_data):
    time = datetime.datetime.now()
    H_open = open(H_path,'a')
    try:
        H_open.write(str(time) + '\t' + H_data + '\n')
        print 'success'
    finally:
        H_open.close()
        print 'closed'
    return

#add Data data
def add_Data(D_data):
    time = datetime.datetime.now()
    D_open = open(D_path,'a')
    try:
        D_open.write(str(time) + '\t' + D_data + '\n')
        print 'success'
    finally:
        D_open.close()
        print 'closed'
    return

#just for test, remove it after test
#create_file()
#add_Heart('just for test')
#add_Data('just for test')

#socket server
#if nessery, we can write down the options result of a file

#for test
x = 0

while True:
    conn,addr = s.accept()
    print 'connect by ',addr
    tp = conn.recv(1024)
    if(tp == '00'):
        conn.sendall('accept_H')
        add_Heart(conn.recv(1024))
    elif(tp == '10'):
        if(x > 2):
            x = 0
            conn.sendall(light[2])
        else:
            conn.sendall(light[x])
            x = x + 1
    elif(tp == '01'):
        conn.sendall('accept_H')
        add_Heart(conn.recv(1024))
    elif(tp == '11'):
        conn.sendall('accpet_D')
        add_Data(conn.recv(1024))
    conn.close()
