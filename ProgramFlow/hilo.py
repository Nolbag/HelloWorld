low = 1
high = 1000

print("Please think of a number between {} and {}: ".format(low, high))
input("Press ENTER to start ")

guesses = 1
while low != high:
    print("\tGussing in the range of {} to {}".format(low, high))
    guess = (low + high) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
    "Enter h or l, or c if my guess was correct "
    .format(guess)).casefold()

    if high_low == "h":
        #Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess +1
        pass
    elif high_low == "l":
        #Guess lower. The high end of the range becomes 1 less than the guess
        high = guess - 1
        pass
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses)) # type: ignore
        break
    else:
        print("Please enter h, l, or c")
    #guesses = guesses +1
    guesses +=1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))