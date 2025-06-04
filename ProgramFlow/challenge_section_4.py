user_options = ["add", "subtract", "multiply", "divide", "quit"]
print("Please select an option from the following list:")
for number, option in enumerate(user_options, start=1):
    print("{}. {}".format(number, option))

while True:
    try:
        user_input = int(input("Please enter your choice: "))
        if user_input == 1:
            print("You have chosen to add")
        elif user_input == 2:
            print("You have chosen to subtract")
        elif user_input == 3:
            print("You have chosen to multiply")
        elif user_input == 4:
            print("You have chosen to divide")
        elif user_input == 5:
            print("You have chosen to quit")
            break
        else:
            print("Invalid option, please try again")
    except ValueError:
        print("Please enter a valid number.")