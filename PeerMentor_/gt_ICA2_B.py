# gt_ICA2_B.py
#        Calculate the total cost of an order including
#        shipping
#       Inputs: Cost of items ordered(Must be positive), repeat
#       Outputs: Shipping cost, Total cost

# By Gentry Trimble

def main():
    # Program name with format of test case
    print("==="*15,'\nShipping Calculator')
    print('==='*15)
    # initializing repeat function of while loop
    repeat = 'y'
    # while loop to repeat the program
    while repeat.lower() == 'y':
        # while loop to verify input
        while True:
            cost = float(input("Cost of items ordered: "))
            if cost < 0:
                print("You must enter a positive number. Please try again")
            else:
                break
        # Control statements after verification of input
        if cost < 30:
            shipcost = 5.95
            total = cost + shipcost
        elif 30 <= cost <= 49.99:
            shipcost = 7.95
            total = cost + shipcost
        elif 50 <= cost <= 74.99:
            shipcost = 9.95
            total = cost + shipcost
        else:
            shipcost = 0
            total = cost
        # Final output from control statements
        print(f"Shipping Cost:{shipcost}\nTotal Cost:{round(total,2)}")
        print('==='*15)
        # reinitialization of repeat function to continue program
        repeat = input("Continue? (y/n): ")
    #End statement in accordance with test case
    print("==="*15,'\n Bye!')

main()


