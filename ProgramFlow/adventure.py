available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

else:
    print("Aren't you glad you got out of there")
# The code above is a simple text-based adventure game where the player can choose a direction to exit.