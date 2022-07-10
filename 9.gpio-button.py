#!/usr/bin/python3
from gpiozero import *
from time import sleep
from signal import *


mybtn = Button(2)


def say_hello():
    print("hello")

mybtn.when_activated = say_hello  


pause()
