#gt_ICA3_C.py
# Program to check whether a number is a prime number and
# display total number of factors if it is not a prime number

# Input: Prime number, repeat

# Output: if number is prime

# By Gentry Trimble
def display_title():
    print("Prime Number Checker")
    # Basic title to be called back in main

def get_valid_int():
    # While loop to check if integers are within range
    while True:
        user = int(input("Enter an integer between 1 and 500:"))
        if 1<user<500:
            break # Passes numbers within defined range to main by breaking loop
        else: print("Invalid Integer. Please try again.")
    return user
def get_factor_count(user):
    prime = ""
    total = 2 # If the user input has two factors then it is prime
    if user > 1:
        # Iterate from 2 to n/2 to
        for i in range(2, int(user / 2) + 1):
            if (user % i) == 0:
                total +=1 # Will not change if prime

        if total == 2:
            print(user, "is a prime number")
        else: print(f'{user} is NOT a prime number.\nIt has {total} factors. ')

def main():
    display_title() # Calls title function
    repeat = "y" # repeat function
    while repeat.lower() == 'y':
        user = get_valid_int() # gathers input from valid input
        get_factor_count(user) # calls the factor counter
        repeat = input(" Chose another integer? (y/n)")
    print("Thank You! Bye!")
main()




