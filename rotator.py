#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys

MYPIN = 40

COUNT = 0

# 初始化树莓派引脚，设置树莓派的引脚为输出状态
def setup():
    GPIO.setwarnings(False)
   # GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MYPIN, GPIO.IN)

# 清除树莓派引脚状态赋值
def destroy():
    GPIO.cleanup()  # 释放数据


def my_callback(channel):
    global  COUNT
    COUNT = COUNT+ 1
    print('the count value is:', COUNT)

def mainprocess():
    #GPIO.add_event_detect(MYPIN, GPIO.FALLING, callback=my_callback)
    while True:
        print('the voltage level is ',GPIO.input(MYPIN))
        time.sleep(1)  # 为 CPU 留出 10 毫秒，供其处理其它事物



if __name__ == '__main__':  # Program start from here
   setup()
   try:
        mainprocess()
   except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
        destroy()
   finally:
        destroy()
