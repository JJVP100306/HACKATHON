from time import sleep 

try: 
    from machine import Pin 
    HARDWARE_MODE = True 
except ImportError:
    HARDWARE_MODE = False 

    class Pin: 
        OUT = 0

        def __init__(self, pin_number, mode):
            self.pin_number = pin_number 
            self.mode = mode
            self.state = 0 

        def value(self, val=None):
            if val is not None:
                return self.state
            self.state = val
            print(f"[MOCK PIN] GP{self.pin_number} set to {val}")

#PIN setup 
#Lift motor pins
lift_in1 = Pin(4, Pin.OUT)
lift_in2 = Pin(5, Pin.OUT) 

#Upper horizontal bridge pins 
horizontal_in1 = Pin(6, Pin.OUT)
horizontal_in2 = Pin(7, Pin.OUT)


#Lift system 
def lift_up():
    print("🚗 Lifting up")
    lift_in1.value(1)
    lift_in2.value(0)   
    
def lift_down():
    print("🚗 Lifting down")
    lift_in1.value(0)
    lift_in2.value(1)

def stop_lift():
    print("🛑 Stopping lift")
    lift_in1.value(0)
    lift_in2.value(0)

#Horizontal system

def horizontal_forward():
    print("🚗 Moving horizontal forward")
    horizontal_in1.value(1)
    horizontal_in2.value(0)

def horizontal_backward():
    print("🚗 Moving horizontal backward")
    horizontal_in1.value(0)
    horizontal_in2.value(1)

def stop_horizontal():
    print("🛑 Stopping horizontal movement")
    horizontal_in1.value(0)
    horizontal_in2.value(0)

# Phase wrappers 
def move_bridge_forward():
    print("🚗 Moving bridge forward")
    horizontal_forward()

def move_car_across():
    print("🚗 Car moving across")
    horizontal_forward()

def move_bridge_backward():
    print("🚗 Moving bridge backward")
    horizontal_backward()



