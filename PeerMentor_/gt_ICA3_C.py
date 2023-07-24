#gt_ICA3_C.py
# guessing game, find and fix all the errors
# gt_ICA3_C.py
# Fix and guessing_game.py
#
#
#
# by Gentry Trimble


import random  # must import random for program to work


def display_title():
    print("Guess the number!")
    print()


def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit


def play_game(limit):
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}\n")

    count = 1 # count must be at 1 since the first try is #1
    while True:
        guess = int(input("Your guess: "))  # must be in int
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:  # cant be equal or greater than or the last elif wont process
            print("Too high.")
            count += 1
        elif guess == number:
            print(f"You guessed it in {count} tries.\n")
            break



def main():
    display_title()

    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game(limit)  # Have to include limit variable within playgame

        again = input("Play again? (y/n): ")
        print()
    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()

