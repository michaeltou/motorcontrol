#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import *
from signal import *

mypin  = 38
mypin_in = 36
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypin,GPIO.OUT)
GPIO.setup(mypin_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)

index = 0
# 清除树莓派引脚状态赋值
def destroy():
    GPIO.cleanup()  # 释放数据

def my_callback(channel):
    global  index
    index = index +1
    print('检测到低电平，端口是: %s'%channel,index)


try:
    GPIO.add_event_detect(mypin_in, GPIO.FALLING, callback=my_callback)

    while True:
        GPIO.output(mypin, GPIO.HIGH)
        sleep(1)
        GPIO.output(mypin, GPIO.LOW)
        sleep(1)

    pause()

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
    destroy()




