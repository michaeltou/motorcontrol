#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

IN1 = 17  # pin40
IN2 = 27
IN3 = 23
IN4 = 24

delay=0.1
step = 4096


def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)


def stop():
    #setStep(0, 0, 0, 0)
    print("stop...")


def forward(delay, steps):
    print("forward...")
    for i in range(0, steps):
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)


def backward(delay, steps):
    print("backward...")
    for i in range(0, steps):
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)



def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)  # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def loop():
    while True:
        backward(delay, step)  # 0.00003为发射脉冲的时间间隔，单位为秒，1000代表发射脉冲的个数


       # time.sleep(3)  # sleep 3s

        forward(delay, step)

        # stop()
        # time.sleep(3)


def destroy():
    GPIO.cleanup()  # 释放数据


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
        destroy()




