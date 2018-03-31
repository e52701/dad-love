import RPi.GPIO as GPIO
import socket
import time

R,G,B=18,15,14
R1,G1,B1 = 2,3,4
R2,G2,B2 = 13,19,26
R_L,G_L,B_L = 0,0,0

GPIO.setmode(GPIO.BCM)

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(G1, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(G2, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)

pwmR = GPIO.PWM(R, 70)
pwmG = GPIO.PWM(G, 70)
pwmB = GPIO.PWM(B, 70)
pwmR1 = GPIO.PWM(R1, 70)
pwmG1 = GPIO.PWM(G1, 70)
pwmB1 = GPIO.PWM(B1, 70)
pwmR2 = GPIO.PWM(R2, 70)
pwmG2 = GPIO.PWM(G2, 70)
pwmB2 = GPIO.PWM(B2, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)
pwmR1.start(0)
pwmG1.start(0)
pwmB1.start(0)
pwmR2.start(0)
pwmG2.start(0)
pwmB2.start(0)

HOST = '192.168.0.8'
PORT = 11010
'''
while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.8',11010))
    s.sendall('10')
    data = s.recv(1024)
    if(data == 'close'):
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        pwmR1.ChangeDutyCycle(0)
        pwmG1.ChangeDutyCycle(0)
        pwmB1.ChangeDutyCycle(0)
        pwmR2.ChangeDutyCycle(0)
        pwmG2.ChangeDutyCycle(0)
        pwmB2.ChangeDutyCycle(0)
    else:
        R_L = data[0:2]
        G_L = data[3:5]
        B_L = data[6:8]
        pwmR.ChangeDutyCycle(int(R_L))
        pwmG.ChangeDutyCycle(int(G_L))
        pwmB.ChangeDutyCycle(int(B_L))
        pwmR1.ChangeDutyCycle(int(G_L))
        pwmG1.ChangeDutyCycle(int(B_L))
        pwmB1.ChangeDutyCycle(int(R_L))
        pwmR2.ChangeDutyCycle(int(B_L))
        pwmG2.ChangeDutyCycle(int(R_L))
        pwmB2.ChangeDutyCycle(int(G_L))
    print 'success'
    s.close()
    time.sleep(1)

'''
try:
    t = 0.4
    while True:
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        pwmR1.ChangeDutyCycle(0)
        pwmG1.ChangeDutyCycle(100)
        pwmB1.ChangeDutyCycle(0)
        pwmR2.ChangeDutyCycle(0)
        pwmG2.ChangeDutyCycle(0)
        pwmB2.ChangeDutyCycle(100)
        time.sleep(t)

except KeyboardInterrupt:
    pass


pwmR.stop()
pwmG.stop()
pwmB.stop()
pwmR1.stop()
pwmG1.stop()
pwmB1.stop()
pwmR2.stop()
pwmG2.stop()
pwmB2.stop()

GPIO.cleanup()
