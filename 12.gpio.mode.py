#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()

print(mode)

pause()
