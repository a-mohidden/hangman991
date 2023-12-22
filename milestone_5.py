import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []

        # Intro to hangman message 
        print(f"The word has {self.num_letters} letters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        letter = letter.lower()

        # Check if the letter is in the word
        if letter in self.word:
            # Replace '_' in the word_guessed list with the letter
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter

            # Reduce the number of unique letters in the word
            self.num_letters -= 1
        else:
            # Reduce the number of lives if the letter is incorrect
            self.num_lives -= 1

    def ask_letter(self):
        while True:
            # Ask the user for a letter iteratively until a valid letter is entered
            letter = input("Please guess a letter: ").lower()

            # Check if the input is a letter
            if len(letter) == 1 and letter.isalpha():
                # Check if the letter has not been tried yet
                if letter in self.list_letters:
                    print(f"{letter} was already inputted.")
                else:
                    # If the letter is valid, call the check_letter method
                    self.list_letters.append(letter)
                    self.check_letter(letter)
                    break
            else:
                print("Please, enter just one letter.")

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    # Iteratively ask the user for a letter until they guess the word or run out of lives
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()
        print(game.word_guessed)

    # Check if the user won or lost
    if '_' not in game.word_guessed:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
