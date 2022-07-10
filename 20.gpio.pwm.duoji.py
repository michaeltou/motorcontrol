#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
p=GPIO.PWM(12,50)
p.start(0)

while 1:
    #angel = int(input('input angel:'))
    #dc=angel/18+3
    for dc in range(3,13,1):
        print('dc is：',dc)
        p.ChangeDutyCycle(dc)
        sleep(1)
    for i in range(1,10): 
        dc= 3.1
        print('dc is：',dc)
        p.ChangeDutyCycle(dc)
        sleep(1)
        dc = 13
        print('dc is：', dc)
        p.ChangeDutyCycle(dc)
        sleep(1)


pause()
p.stop()
GPIO.cleanup()


