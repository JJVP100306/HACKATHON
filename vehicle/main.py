from movement import forward, backward, stop

while True:
    command = input("Enter command (F, B, S): ").strip().upper()

    if command == "F":
        forward()
    elif command == "B":
        backward()
    elif command == "S":
        stop()
    else:
        print("Invalid command")