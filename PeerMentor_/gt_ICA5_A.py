#gt_ICA5_A.py
# Exception Handling, Prime number checker
# input: any numerical value
# output: if value is an integer between 1-500,
#       if not prime then factors are outputed
# this is a continuation of ICA4_A


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
        try:
            num = int(input("Please enter an integer between 1 and 500: "))
            if 1<num<500:
                break
            else: print("Invalid integer. Try again.")
        except ValueError: # this is the check on the value errors, ie lack of input or not in range
            print('Invalid or no input. Try again.')


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