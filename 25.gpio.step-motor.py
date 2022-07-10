#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

delay = 2
pin_4 = 4
pin_17 = 17
pin_23 = 23
pin_24 = 24

GPIO.setmode(GPIO.BCM)

def init():
    GPIO.setwarnings(False)
    GPIO.setup(pin_4,GPIO.OUT)
    GPIO.setup(pin_17,GPIO.OUT)
    GPIO.setup(pin_23,GPIO.OUT)
    GPIO.setup(pin_24,GPIO.OUT)

def moveOnestep(w1,w2,w3,w4):
    GPIO.output(pin_4,w1)
    GPIO.output(pin_17, w2)
    GPIO.output(pin_23, w3)
    GPIO.output(pin_24, w4)

def forward(delay):
    moveOnestep(1,0,0,0)
    time.sleep(delay)
    moveOnestep(0, 1, 0, 0)
    time.sleep(delay)
    moveOnestep(0, 0, 1, 0)
    time.sleep(delay)
    moveOnestep(0, 0, 0, 1)
    time.sleep(delay)


init()
while True:
    forward(int(delay) / 1000.0)
