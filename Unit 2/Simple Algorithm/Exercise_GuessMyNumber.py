print("Please think of a number between 0 and 100!")
low = 0
high = 100
mid = int((low + high)/2)
print("Is your secret number " + str(mid) + "?")
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while guess.lower() != "c":
    if guess.lower() == "h":
        high = mid
        mid = int((low + high)/2)
        print("Is your secret number " + str(mid) + "?")
    elif guess.lower() == "l":
        low = mid
        mid = int((low + high)/2)
        print("Is your secret number " + str(mid) + "?")
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(mid) + "?")

    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: " + str(mid))

