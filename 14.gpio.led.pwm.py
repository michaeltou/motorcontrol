#!/usr/bin/python3
import RPi.GPIO as GPIO

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

p=GPIO.PWM(12,0.5)

p.start(80)

input('press return to stop:')

p.stop()


GPIO.cleanup()


