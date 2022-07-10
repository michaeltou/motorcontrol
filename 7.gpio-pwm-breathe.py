#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *

myled = PWMLED(17)

myled.pulse()

pause()



