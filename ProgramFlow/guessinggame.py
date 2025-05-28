import random

highest = 1000
answer = random.randint(1, highest)
# answer = random.randint(1, 10) # This line generates a random number between 1 and 10
print (answer)
guess = 0 # guess is initialized to 0 so that the while loop can start
print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("You have chosen to quit the game")
        print("The answer was {}".format(answer))
    break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
        print("Well done, you guessed it")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
# The code below is an alternative way to write the same logic, but it is less efficient

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it") 
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

