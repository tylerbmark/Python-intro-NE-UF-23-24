#gt_ICA4_A.py
# Program that checks whether a number is a prime number and displays it's factors if it is not a prime number
# Input: Valid number between 1 and 500
#  Output: Prime numbers and whether or not prime

# by Gentry Trimble

def display_Title():
    print("Prime Number Checker\n")
# title


def get_factors(num):
    str_ = ""
    factors = []
    #initialize the list
    if num > 1: # check if prime and gather factors
        for i in range(1,int(num)+1):
            if (num%i) == 0:
                factors.append(i)
        if len(factors) >2:
            print(f"{num} is NOT a prime number.")

            for i in factors:
                if i != len(factors):
                    str_ += str(i) + ", "
            print(f"{num} has {len(factors)} factors: {str_[:-2]}")


        else: print(f"{num} is a prime number")


def get_valid_int(): # input validation
    while True:
        num = int(input("Please enter an integer between 1 and 500: "))
        if 1<num<500:
            break
        else: print("Invalid integer. Try again.")

    return num

def main(): # simple main to combine all functions
    display_Title()
    repeat = "y"
    while repeat.lower() == 'y':

        num = get_valid_int()

        get_factors(num)

        repeat = input("\nCheck another integer? (y/n):")
        print()
    print("\nThank you ! Bye!")
main()