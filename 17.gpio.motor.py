#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
p=GPIO.PWM(12,400)
p.start(0)

while 1:
    for dc in range(100): 
        print('dc：',dc)
        p.ChangeDutyCycle(dc)
        sleep(0.3)



pause()

p.stop()
GPIO.cleanup()


