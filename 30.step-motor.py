#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# w1,w2,w3,w4,w5,w6 = 0,1,0,0,0,0,0   细分400，电流3.5A，电压24V
IN1 = 20  # 接PUL-
IN2 = 21  # 接PUL+
IN3 = 12  # 接DIR-
IN4 = 16  # 接DIR+


IN5 = 19  # 接ENA-
IN6 = 26  # 接ENA+


def setForwardMode():
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)

def setBackwardMode():
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)


def setValue(w1, w2):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)

##触发一次脉冲，
def goForOneStep(delay):
    #这种脉冲方式方式，是pul+,pul-，分别接一个GPIO接口，测试ok。pul+,pul-置换高低电位变化差达3.3v*2=6.6v
    setValue(1, 0)
    time.sleep(delay)
    setValue(0, 1)
    time.sleep(delay)

    #下面这种脉冲方式，是对接PUL+接树莓派3.3v，pul-接GPIO，测试ok，pul+,pul-置换高低电位差可达3.3v
    # GPIO.output(IN1, 0)
    # time.sleep(delay)
    # GPIO.output(IN1, 1)
    # time.sleep(delay)

    #这种脉冲方式方式，是pul+,pul-，分别接一个GPIO接口，测试ok。pul+,pul-置换高低电位差可达3.3v
    # setValue(0, 1)
    # time.sleep(delay)
    # setValue(1, 1)
    # time.sleep(delay)


# 初始化树莓派引脚，设置树莓派的引脚为输出状态
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(IN5, GPIO.OUT)
    GPIO.setup(IN6, GPIO.OUT)


def stop():
    setValue(0, 0)

# 正转
# 控制电机旋转的快慢和圈数 delay越小转得越快，1600为一圈
def forward(delay, steps):
    setForwardMode()
    for i in range(0, steps):
        goForOneStep(delay)



# 反转
# 控制电机旋转的快慢和圈数 delay越小转得越快，1600为一圈
def backward(delay, steps):
    setBackwardMode()
    for i in range(0, steps):
        goForOneStep(delay)

#通过控制使能ENA，锁定电机
def lock():
    GPIO.output(IN5, 1)
    GPIO.output(IN6, 0)

#通过控制使能ENA，释放电机
def unlock():
    GPIO.output(IN5, 0)
    GPIO.output(IN6, 1)

# 检测正转和反转
def loop():
    while True:
        i=int(input("1、正转\t2、反转\t3、退出\t4、锁定\t5、释放\n请输入数字： "))
        if i==1:
            b = 16000 #int(input("请输入脉冲个数（1600个脉冲为一圈）："))
            forward(0.00001, b)
            #print("请等待3秒...")
            #time.sleep(3)
            print("stop...")
            stop()
        elif i==2:
            a=16000 #int(input("请输入脉冲个数（1600个脉冲为一圈）："))
            backward(0.00001, a)  # 发射脉冲时间间隔0.0001（单位秒）   脉冲个数a 如果编码器的设置是8细分 那么1600冲就转360度
            #print("请等待3秒...")
            #time.sleep(3)
            print("stop...")
            stop()  # stop
        elif i == 4:
            #锁定
            lock()
        elif i == 5:
            #释放
            unlock()
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
