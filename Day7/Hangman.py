'''
links=>
https://en.wikipedia.org/wiki/Hangman_(game)
https://developers.google.com/edu/python/lists#for-and-in
https://developers.google.com/edu/python/lists#range
https://www.askpython.com/python/python-import-statement


'''
import random

stages = ['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
 +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
+---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
+---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["camel", "typhoon", "rain", "python", "learning"]

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

print("Word to guess:", " ".join(display))

game_over = False
guessed_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("🎉 You win!")

    if lives == 0:
        game_over = True
        print("💀 You lose.")
        print(f"The word was: {chosen_word}")
