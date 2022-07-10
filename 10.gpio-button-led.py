#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *


myled = PWMLED(17)

mybtn = Button(2)


def say_hello():
    print("hello")
    if myled.is_active:
        myled.off()
    else:
        myled.on()

mybtn.when_activated = say_hello


pause()
