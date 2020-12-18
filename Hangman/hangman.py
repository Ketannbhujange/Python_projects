import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word  = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives  = 6
    while len(word_letters)!=0 and lives>0:
        # #lives completed
        # if lives==0:
        #     print('All lives used .Restart the game!!!')
        #     break;
        #letters already used
        print('You have already used these letters: ',' '.join(used_letters))
        #what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ',' '.join(word_list))
        #getting input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f'You have guessed the wrong letter!.Lives Remaining {lives}')
        elif user_letter in used_letters:
            print('You have already used that character. Please Try Again!')
        
        else:
            print('Invalid cahracter! PLease try again!!')
    if lives==0:
        print(f"Sorry!! all your lives are over!! The word was {word}")
    else:
        print("Yay! You guessed the word correctly!!")
    
    
hangman()