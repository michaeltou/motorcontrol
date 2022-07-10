#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *

 

buzzer = PWMLED(3)


buzzer.pulse()


pause()
