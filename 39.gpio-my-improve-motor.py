#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys

PUL = 38  # 接PUL-



# 初始化树莓派引脚，设置树莓派的引脚为输出状态
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PUL, GPIO.OUT)


def stop():
     print('stop')


##触发一次脉冲，
def goForOneStep(delay):
    GPIO.output(PUL, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(PUL, GPIO.HIGH)
    time.sleep(delay)

# 正转
# 控制电机旋转的快慢和圈数 delay越小转得越快，1600为一圈
def forward(delay, steps):
     for i in range(0, steps):
        goForOneStep(delay)

# 反转
# 控制电机旋转的快慢和圈数 delay越小转得越快，1600为一圈
def backward(delay, steps):
     for i in range(0, steps):
        goForOneStep(delay)


# 检测正转和反转
def loop():
    while True:
        #i=int(input("1、正转\t2、反转\t3、退出\t4、锁定\t5、释放\n请输入数字： "))
        i=1
        if i==1:
            b = 16000 #int(input("请输入脉冲个数（1600个脉冲为一圈）："))
            #forward(float(sys.argv[1]), b)
            forward(0.01, b)
            print("stop...")
            stop()
        elif i==2:
            a=16000 #int(input("请输入脉冲个数（1600个脉冲为一圈）："))
            backward(float(sys.argv[1]), a)  # 发射脉冲时间间隔0.0001（单位秒）   脉冲个数a 如果编码器的设置是8细分 那么1600冲就转360度
            #print("请等待3秒...")
            #time.sleep(3)
            print("stop...")
            stop()  # stop
        else:
            destroy()
            return

# 清除树莓派引脚状态赋值
def destroy():
    GPIO.cleanup()  # 释放数据

if __name__ == '__main__':  # Program start from here
   setup()
   try:
        loop()
   except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
        destroy()
