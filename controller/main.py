#Joystick input, sendind commands 
from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)  # more reliable than "LED"

while True:
    led.toggle()
    sleep(0.5)