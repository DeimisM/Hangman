
import random

                # variable for checking if the user has guessed the word
is_word_guessed = False
guesses_left = 10

                # takes a list and chooses a random word from the list
                    # python is tab sensitive, so "\" is used as a line continuation character to allow us to break a long line of code without causing errors
word_list = \
[
    "python", "giraffe", "keyboard", "puzzle", "mystery",
    "balloon", "adventure", "elephant", "champion", "umbrella",
    "treasure", "penguin", "dinosaur", "galaxy", "whistle",
    "notebook", "volcano", "rainbow", "sapphire", "journey"
]

word = random.choice(word_list)         # choose a random word from the word list
word_letters = list(word)               # convert the word into a list of letters        # also ... = [*word] works the same
word_length = len(word)                 # word length
display_word = ["_ "] * word_length

#print(word_letters)
                                        # welcome message
print("\nWelcome to Hangman!\nYou must try to guess the letters of the word before you get hanged!\n")

                #code block for processing guesses
while is_word_guessed != True:

    if guesses_left > 0:
        print("\nCurrent word: " + " ".join(display_word))                  # shows current progress
        print("You have", guesses_left, "guesses left.")
                                                                            # takes user input (user's guess)
        users_guess = input("\nTry to guess the letters of the word:")

        if users_guess.isalpha() and len(users_guess) == 1:
            if users_guess in word_letters:
                print(f"\t{users_guess} is IN the word!")

                for index, letter in enumerate(word_letters):               # Replace underscores with the guessed letter in the correct positions
                    if letter == users_guess:
                        display_word[index] = users_guess                   # update the displayed word

                if "_ " not in display_word:
                    is_word_guessed = True

            elif users_guess not in word_letters:
                print(f"\t{users_guess} is NOT IN the word!")
                guesses_left -= 1                                           # reduce guesses left if didn't guess right

        else:
            print("\tYour guess must only include 1 letter!")

    else:
        print("\nYou lost! The word was:", word)
        break

if is_word_guessed == True:
    print("\n\nYou have won the game! Congratulations!\nThe word was:", word)

#print(word)
#print(word_length)



