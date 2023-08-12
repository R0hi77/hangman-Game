import random
import ascii
import wordList

# generating a random choice form the list of words
chosen_word = random.choice(wordList.words)

display = ["_"]
# creating the empty string

for char in range(0, len(chosen_word)-1):
    display.append("_")

# print(chosen_word)
print(ascii.logo)
print("")
print(display)

end_of_game = False
lives = 6
counter = 6

while not end_of_game:

    guess = input("Hey! guess the letters in the word above :")

    for position in range(len(chosen_word)):
        char = chosen_word[position]
        if guess == char:
            display[position] = char



    if guess not in chosen_word:
            lives -= 1
            counter -= 1
            print(f"You guessed the letter {guess} ")
            print(f"You have {lives} left")
            print(ascii.Hangman[counter])

            if lives == 0:
                end_of_game = True
                print("Sorry! You loose")
    if guess in display:
        print("you have already guessed this letter")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("Hurray! You win")





