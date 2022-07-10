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
        sleep(0.5)
    for i in range(1,20):
        dc= 3.5
        print('dc is：',dc)
        p.ChangeDutyCycle(dc)
        sleep(0.5)
        dc = 13
        print('dc is：', dc)
        p.ChangeDutyCycle(dc)
        sleep(0.5)


pause()
p.stop()
GPIO.cleanup()


