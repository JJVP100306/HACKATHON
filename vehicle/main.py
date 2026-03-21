# main.py
from vehicle import commands, movement

print("Robot ready")
movement.stop()  # default

while True:
    cmd = input("Enter command: ").strip()
    commands.execute_command(cmd)