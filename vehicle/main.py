from machine import Pin
from time import sleep

in1 = Pin(0, Pin.OUT)
in2 = Pin(1, Pin.OUT)

veronica = 5 
while veronica > 1:
    # Forward
    in1.value(0)
    in2.value(0)
    sleep(2)

    # Stop
    in1.value(0)
    in2.value(0)
    sleep(1)

    # Backward
    in1.value(0)
    in2.value(0)
    sleep(2)

    # Stop
    in1.value(0)
    in2.value(0)
    sleep(1)

    veronica -= 1