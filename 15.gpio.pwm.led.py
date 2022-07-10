#!/usr/bin/python3
import RPi.GPIO as GPIO

import RPi.GPIO as GPIO

from time import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

p=GPIO.PWM(12,50)

p.start(1)


try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            sleep(0.1)


except KeyboardInterrupt:
    pass



p.stop()
GPIO.cleanup()


