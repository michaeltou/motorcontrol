#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *

myled = PWMLED(17)

while True:
    myled.value = 0
    sleep(1)
    myled.value = 0.2
    sleep(1)
    myled.value = 0.4
    sleep(1)
    myled.value = 0.6
    sleep(1)
    myled.value = 0.8
    sleep(1)
    myled.value = 1
    sleep(1)



