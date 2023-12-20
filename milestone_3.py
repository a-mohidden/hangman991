import random 

word_list = ["apple", "pear", "grape", "mango", "orange"]
word = random.choice(word_list)

potential_word = []
for space in range(len(word)):
  potential_word += '_'


def ask_for_input():
  guess = input("Please type a letter. " )
  guess = guess.lower()
  if len(guess) == 1 and guess.isalpha():
    print("That is a valid input.")
    return guess
  else:
    print("Oops, that isn't a valid input!")



def check_guess(guess):
  for l in range(len(word)):
    letter = word[l]
    if letter == guess:
      potential_word[l] = letter
  # word_checker acts as a control
  word_checker = []
  for space in range(len(word)):
    word_checker += '_'
  if potential_word == word_checker:
    print(f"Sorry, {guess} is not in the word. Try again.")
    return potential_word
  else:
    print(f"Good guess! {guess} is in the word.")
    return potential_word



the_end = False
while not the_end: 
  guess = ask_for_input()
  potential_word = check_guess(guess)
  print(potential_word)
  if '_' not in potential_word:
    the_end = True
    print("You have won!")
