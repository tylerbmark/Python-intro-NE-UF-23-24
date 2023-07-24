# gt_ICA2_C.py
#
# print a staircase of stairs oriented in a direction
# depending on the user input

#   Input: Option of orientation, repeat
#
#   Output: Staircase of strings
def main():
    #Program Name
    print("Staircase Printer")
    # Initializing repeat function
    repeat = 'y'
    stars = 6 # Amount of stars for the staircase
    # While loop to continue the program after first use
    while repeat.lower() == "y":
        # while loop to check to ensure options remain within parameters
        while True:
            choice = float(input("Chose an option (1,2,3) :"))
            if 0 < choice < 4:
                break # Once input is verified,loop is broken to go through control statements
            else: print("You must enter 1, 2, or 3. Please try again.")
        # Each if statement is a different variation of stairs
        if choice == 1:# upward left staircase
            for row in range(0, stars):
                for col in range(0, stars):
                    if row >= col:
                        print("* ", end='')
                    else:
                        print("", end="")
                print()

        elif choice == 2: # upsidedown inverted staircase
            for row in range(stars):
                for col in range(stars):
                    if col >= row:
                        print("* ", end="")
                    else:
                        print("", end="")
                print()
        elif choice == 3: # upward right staircase
            for row in range(stars+1 ):
                for col in range(stars , 0, -1):
                    if col > row:
                        print(" ", end=" ")
                    else:
                        print("* ", end="")
                print()

        repeat = input("Continue? (y/n): ") # input value to repeat program
    if repeat.lower() == 'n':
            # End message
            print("\nBye!")

main()

