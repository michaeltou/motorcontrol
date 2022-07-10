#!/usr/bin/python3
from gpiozero import *
from time import sleep

myled = LED(17)

while True:
    myled.on()
    
