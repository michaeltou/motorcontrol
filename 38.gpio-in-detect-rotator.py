#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

mypin_out_38  = 38
#编码器信号1
mypin_in_36 = 36
#编码器信号2
mypin_in_32 = 32

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypin_out_38,GPIO.OUT)
GPIO.setup(mypin_in_36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(mypin_in_32, GPIO.IN, pull_up_down=GPIO.PUD_UP)


index = 0
# 清除树莓派引脚状态赋值
def destroy():
    GPIO.cleanup()  # 释放数据

def my_callback(channel):
    global  index
    index = index +1
    print('检测到低电平，端口是: %s'%channel,index)
    if GPIO.input(mypin_in_32) == GPIO.HIGH:
        print('电机正转~~~~~~~~~~~~~~~~~~')
    else:
        print('电机逆转*******')

try:
    GPIO.add_event_detect(mypin_in_36, GPIO.FALLING, callback=my_callback)

    while True:
        GPIO.output(mypin_out_38, GPIO.HIGH)
        sleep(1)
        GPIO.output(mypin_out_38, GPIO.LOW)
        sleep(1)

    pause()

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
    destroy()




