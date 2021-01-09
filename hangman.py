import random
import hangman_words
# from replit import clear

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art

logo = hangman_art.logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letters = ""
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display or guess in guessed_letters:
      print(f"You have already guessed \"{guess}\"...")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in word. You lose a point")
        lives -= 1
        guessed_letters += guess
        if lives == 0:
            end_of_game = True
            print(f"Uh ooh...The chosen word was {chosen_word}.")
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages = hangman_art.stages
    print(stages[lives])