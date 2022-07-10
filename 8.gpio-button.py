#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *


mybtn = Button(2)


while True:
    if mybtn.is_active:
        print("button is pressed")
    else:
        print("button is not pressed")

    sleep(1)
