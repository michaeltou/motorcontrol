#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *

myled = LED(17)

myled.blink()

pause()

