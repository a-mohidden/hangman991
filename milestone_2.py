import random 

word_list = ["Apple", "Pear", "Grape", "Mango", "Orange"]
word = random.choice(word_list)

guess = input("Please type a letter. " )
guess = guess.lower()

if len(guess) == 1 and guess.isalpha():
  print("Good guess!")
else:
  print("Oops, that isn't a valid input!")
