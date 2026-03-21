from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)   # 25 is built-in LED on many boards (like Pico)

while True:
    led.value(1)   # ON
    sleep(1)
    led.value(0)   # OFF
    sleep(1)