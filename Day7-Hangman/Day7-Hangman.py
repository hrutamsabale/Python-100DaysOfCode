#This requires importing both hangman_words.py and hangman_art.py
#Link to hangman_words.py: https://replit.com/@appbrewery/Day-7-Hangman-5-Start#hangman_words.py
#Link to hangman_art.py: https://replit.com/@appbrewery/Day-7-Hangman-5-Start#hangman_art.py
import random
import hangman_words
import hangman_art

word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already entered '{guess}'")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"'{guess}' is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!!!!!!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!!!!!!")

    print(hangman_art.stages[lives])
