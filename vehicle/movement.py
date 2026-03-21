def forward():
    print("Moving forward")

def backward():
    print("Moving backward")

def stop():
    print("Stopping")


from machine import Pin

#placeholders 
in1 = none #cambiar 
in2 = none #cambiar por pins later 

def forward():
    in1.value(1)
    in2.value(0)
    print("Moving forward")

def backward():
    in1.value(0)
    in2.value(1)
    print("Moving backward")

def stop():
    in1.value(0)
    in2.value(0)
    print("Stopping")
