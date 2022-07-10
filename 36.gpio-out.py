#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

mypin  = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypin,GPIO.OUT)
GPIO.setwarnings(False)


# 清除树莓派引脚状态赋值
def destroy():
    GPIO.cleanup()  # 释放数据


try:
    while True:
        GPIO.output(mypin, GPIO.HIGH)
        sleep(1)
        GPIO.output(mypin, GPIO.LOW)
        sleep(1)

    pause()

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
    destroy()




