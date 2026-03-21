from vehicle import movement

def execute_command(cmd):
    if cmd == "forward":
        movement.forward()
    elif cmd == "backward":
        movement.backward()
    elif cmd == "stop":
        movement.stop()
    else:
        print("Unknown command:", cmd)