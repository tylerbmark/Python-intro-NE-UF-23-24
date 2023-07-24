#gt_ICA2_A.py
#       Change Calculator: Calculate he coins needed to make change for the
#       specified number of cents
#   Input: # of Cents, Try again?
#   Outputs:
#   Number of coins:
#   Quarters,Dimes, Nickels,Pennies
#By Gentry Trimble

def main():
    print("Change Calculator")
    # To initialize the while loop and confirm boolean
    repeat = 'y'
    while repeat.lower() == "y":
        # Gather Cent Input
        cent = int(input("Enter number of cents (0 - 99): "))
        # If there is enough for quarters, program will gather
        quarter = cent // 25
        # Redefine cents after quarters are removed
        cent %= 25
        # Same idea with dimes,nickels and pennies
        dime = cent // 10

        cent %= 10

        nickel = cent // 5

        pennies = cent % 5
        # print final output of results
        print(f"Quarters: {quarter}\nDimes: {dime}\nNickels: {nickel}\nPennies: {pennies}")
        # reinitialization of repeat variable for while loop
        repeat = input("Continue? (y/n): ")
    print("\nBye!")
main()

