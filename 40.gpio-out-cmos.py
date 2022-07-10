#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

mypin  = 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypin,GPIO.OUT)


# 清除树莓派引脚状态赋值
def destroy():
    #GPIO.cleanup()  # 释放数据
    print('destroy nothing')
try:

    while True:
        GPIO.output(mypin, GPIO.HIGH)
        sleep(0.000000001)
        GPIO.output(mypin, GPIO.LOW)
        sleep(0.0006)

    #pause()

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
    GPIO.output(mypin, GPIO.LOW)
    destroy()




