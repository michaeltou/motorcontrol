#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

pul_pin  = 38
dir_pin = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pul_pin,GPIO.OUT)
GPIO.setup(dir_pin,GPIO.OUT)



# 清除树莓派引脚状态赋值
def destroy():
    #GPIO.cleanup()  # 释放数据
    print('destroy nothing')
try:
    while True:
        ##设置方向为低电平
        GPIO.output(dir_pin, GPIO.HIGH)

        #下面为一个脉冲
        GPIO.output(pul_pin, GPIO.HIGH)
        sleep(0.00001)
        GPIO.output(pul_pin, GPIO.LOW)
        sleep(0.0006)


except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
    GPIO.output(pul_pin, GPIO.LOW)
    destroy()




