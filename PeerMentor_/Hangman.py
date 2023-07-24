# Hangman game

# for students

# modules to create
'''main()
play_game()
get_word()
draw_screen()
get_letter()
get_random_word()
add_spaces()
'''

import random
words = ['exodus', 'jukebox','waltz', 'potato', 'espionage',
         'fuzzy', 'batman', 'watch', 'Python',
         'anaconda']

def get_random_word():
    word = random.choice(words)
    return word

def get_word():
    return get_random_word().upper()

def add_space(word):
    word_space = ' '.join(word)
    return word_space

def draw_screen(num_wrong,num_guesses,guessed_letters, display_word):
    print('-'*75)
    print(f"Word:  {add_space(display_word)} \t Guesses: {num_guesses}  Wrong: {num_wrong}  Tried: {add_space(guessed_letters)} ")

def get_letter(guessed_letter):
    while True:
        guess = input("Enter a letter: ").strip().upper()
        if guess == "" or len(guess) > 1:
            print("Invalid Entry. Please enter one and only one letter")
            continue
        elif guess in guessed_letter:
            print("You've already tried that letter.")
            continue
        else: return guess

def play_game():
    word = get_word()
    word_length = len(word)
    remaining = word_length
    displayed_word = "_" * word_length
    num_wrong = 0
    num_guesses = 0
    guessed_letter = ''
    draw_screen(num_wrong,num_guesses,guessed_letter,displayed_word)
    while num_wrong < 10 and remaining > 0:
        guess = get_letter(guessed_letter)
        guessed_letter += guess
        pos = word.find(guess,0)
        if pos != -1:
            displayed_word = ''
            remaining = word_length
            for char in word:
                if char in guessed_letter:
                    displayed_word +=char
                    remaining -=1
                else:
                    displayed_word += "_"
        else:
            num_wrong +=1
        num_guesses +=1
        draw_screen(num_wrong,num_guesses,guessed_letter,displayed_word)
    print("-" *75)
    if remaining == 0:
        print(f"Congrats! you did it in {num_guesses} guesses. ")
    else: print(f'Sorry you lost, the word was {word}')
def main():
    print("Play H A N G M A N")
    while True:
        play_game()
        print()
        again = input(" Would you like to play again? (y/n)").lower()
        if again != 'y':
            break
main()