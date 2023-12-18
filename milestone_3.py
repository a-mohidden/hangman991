while True:
    # User input letter
    guess = input("Guess a letter: ")

    # Check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        # Break out of the loop if the guess is a single letter alphabet
        break
    else:
        # Print message for invalid input
        print("Invalid letter. Please, enter a single alphabetical character.")

# The valid guess is now stored in the 'guess' variable outside the loop
print("You guessed:", guess)
