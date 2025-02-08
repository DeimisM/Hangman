
import random

def game():

    # takes a list and chooses a random word from the list
                        # python is tab sensitive, so "\" is used as a line continuation character to allow us to break a long line of code without causing errors
    word_list = \
    [
        "python", "giraffe", "keyboard", "puzzle", "mystery",
        "balloon", "adventure", "elephant", "champion", "umbrella",
        "treasure", "penguin", "dinosaur", "galaxy", "whistle",
        "notebook", "volcano", "rainbow", "sapphire", "journey"
    ]

    is_word_guessed = False                 # variable for checking if the user has guessed the word
    starting_guesses = 10                   # variable for setting the guesses at the start
    guesses_left = starting_guesses         # variable for counting how many guesses the user has


    word = random.choice(word_list)         # choose a random word from the word list
    word_letters = list(word)               # convert the word into a list of letters        # also ... = [*word] works the same
    word_length = len(word)                 # word length
    display_word = ["_ "] * word_length     # variable for showing the word progress display
    incorrect_letters = []                  # variable for showing already guessed incorrect letters


    #print(word_letters)
                                            # welcome message
    print("\n\033[34mWelcome to Hangman!\033[0m\nYou must try to guess the letters of the word before you get \033[31mhanged\033[0m!\n")

                                            #code block for processing guesses
    while is_word_guessed != True:

        if guesses_left > 0:
            print("\nCurrent word: " + "\033[32m", " ".join(display_word), "\033[0m")                  # shows current progress
            print("You have \033[31;4m" + str(guesses_left) + "\033[0m guesses left.")

            if incorrect_letters:                                               # checks if the list is not empty
                print("\033[31mIncorrect letters:", *incorrect_letters,"\033[0m")

                # takes user input (user's guess)
            users_guess = input("\nTry to guess the letters of the word:")

            if users_guess.isalpha() and len(users_guess) == 1:
                if users_guess in word_letters:
                    print(f"\t{users_guess} is \033[32mIN\033[0m the word!")

                    for index, letter in enumerate(word_letters):               # Replace underscores with the guessed letter in the correct positions
                        if letter == users_guess:
                            display_word[index] = users_guess                   # update the displayed word

                    if "_ " not in display_word:
                        is_word_guessed = True

                elif users_guess not in word_letters:
                    print(f"\t{users_guess} is \033[31mNOT IN\033[0m the word!")
                    guesses_left -= 1                                           # reduce guesses left if didn't guess right

                    incorrect_letters += users_guess

            else:
                print("\tYour guess must \033[31monly\033[0m include 1 letter!")

        else:
            print("\nYou \033[31mlost\033[0m! The word was:\033[33m", word, "\033[0m")
            break

    if is_word_guessed:
        print("\n\n\033[32mYou have won the game! Congratulations!\033[0m\nThe word was:\033[33m", word, "\033[0m")

game()


#print(word)
#print(word_length)



