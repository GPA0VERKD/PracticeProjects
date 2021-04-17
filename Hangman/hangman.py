import random
from words import options
import string

def get_valid_word(options):
    word = random.choice(options)
    while "-" in word or " " in word:
        word = random.choice(options)
    return word.upper()

# def drawing(count):
#     a1 = ["0", ".", "0"]
#     a2 = ["/", "|", "\\"]
#     a3 = ["/", " ", "\\"]
#     body_parts = ["0", ".", "0", "|", "/", "\\", "/", "\\"]
#     for x in range(count):

    
#     print("  _____ ")
#     print(" ", a1, "   |")
#     print(" ", a2, "   |")
#     print(" ", a3, "   |")
#     print(" -------")

def hangman():
    word = get_valid_word(options)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # tracks user guess
    count = 0
    # getting user input
    while len(word_letters) > 0 and count < 10:
        print("You have", 10 - count, "chances!")
        print("You have used these letters: ", ",  ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct guess!")
            else:
                print("Incorrect, Try again!")
                count += 1
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")
        print()

    print("The word was", word)
    if count == 10:
        print("You lose!")
    else:
        print("You Win!")


hangman()