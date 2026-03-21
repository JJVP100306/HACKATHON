from machine import Pin
from time import sleep

in3 = Pin(0, Pin.OUT)
in4 = Pin(1, Pin.OUT)

def motor_forward():
    in3.value(1)
    in4.value(0)

def motor_backward():
    in3.value(0)
    in4.value(1)

def motor_stop():
    in3.value(0)
    in4.value(0)

test = 5

while test > 1:
    motor_forward()
    sleep(2)

    motor_stop()
    sleep(1)

    motor_backward()
    sleep(2)

    motor_stop()
    sleep(1)

    test -= 1
    