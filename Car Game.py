command = ""

while True:
    command = input(">").lower()
    if command == "start":
        print("Car is started...")
    elif command == "stop":
     print("Car is stopped...")
    elif command == "help":
     print("""
    command to play the Game:
    start - to start a car
    stop - to stop a car
    quit - to quit the game
    """)
    elif command == "quit":
     break
    else:
     print("Sorry, i understand your keyword take help command")
