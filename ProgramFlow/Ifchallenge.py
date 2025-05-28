name = input("What is your name? ")
if name:
    print("Hello, {}".format(name))
age = int(input("How old are you? "))
if 18 <= age <= 30:
    print("Welcome to your holiday")
else:
    print("You are not allowed to join this holiday")
# The code above checks if the age is between 18 and 30 (inclusive). If it is, it welcomes the user to their holiday;
# otherwise, it informs them that they are not allowed to join the holiday.