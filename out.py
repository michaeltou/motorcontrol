#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

mypin  = 29 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypin,GPIO.OUT)


# 清除树莓派引脚状态赋值
def destroy():
    GPIO.cleanup()  # 释放数据


try:
    GPIO.output(mypin, 1)

    pause()

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
    destroy()




