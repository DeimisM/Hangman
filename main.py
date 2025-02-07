import random


is_word_guessed = False

word_list = [
    "python", "giraffe", "keyboard", "puzzle", "mystery",
    "balloon", "adventure", "elephant", "champion", "umbrella",
    "treasure", "penguin", "dinosaur", "galaxy", "whistle",
    "notebook", "volcano", "rainbow", "sapphire", "journey"
            ]

word = random.choice(word_list)
word_letters = [*word]

#print(word_letters)

#word_length = len(word)

while is_word_guessed != True:
    users_guess = input("\n Try to guess the letters of the word:")

    if users_guess.isalpha() & len(users_guess) == 1:
        if users_guess in word_letters:
            print("\t", users_guess, "is in the word!")

        elif users_guess not in word_letters:
            print("\t", users_guess, "is not in the word.")
    else:
        print("\t", "Your guess must only include 1 letter!")

#print(word)
#print(word_length)



