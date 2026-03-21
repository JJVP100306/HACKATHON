from machine import Pin
from time import sleep

#Left motor 
in3 = Pin(0, Pin.OUT)
in4 = Pin(1, Pin.OUT)

#Right motor
in1 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.OUT)


#---Movement funcitons----

def forward():
    print("🚗 Moving forward")
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    
def backward():
    print("🚗 Moving backward")
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)

def stop():
    print("🛑 Stopping")
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

# #---Testing the movement functions---
# test = 5
# while test > 0:
#     forward()
#     sleep(2)
#     backward()
#     sleep(2)
#     stop()
#     sleep(1)
#     test -= 1