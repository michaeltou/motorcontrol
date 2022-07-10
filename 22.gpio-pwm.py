#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *

myled = PWMLED(17)

while True:
    myled.value = 0.4
    sleep(1)



