#gt_HW1_A.py
# Estimate probability of rolling five of a kind in a single roll of five
# six sided die
# Input: Number of rolls
# Output: Estimated probability


#By: Gentry Trimble
import random
random.seed(42)
import matplotlib.pyplot as plt
def dice():
    # a roll of a six sided die
    return random.randrange(1,7)
def fiverolls():
    # initalizes five different rolls
    d1 = dice()
    d2 = dice()
    d3 = dice()
    d4 = dice()
    d5 = dice()
    return d1,d2,d3,d4,d5
def equal_rolls(n):
    fivetrue = ''
    count = 0
    for i in range(n):
        # After n being verified within the main, it is set as the number of times 5 dice are rolled
        d1,d2,d3,d4,d5 = fiverolls()
        if d1 == d2 and d1 == d3 and d1 == d4 and d1 == d5:
            # checking to see if all five rolls are the same
            fivetrue = True
            count +=1 # if so then each five rolls of five are counted
    if fivetrue == True:
        return True, count # returns the boolean and count to be used in the main
    else: return False,0

def main():
    count = 50
    print("Let's estimate the probability of rolling five of a kind on a single roll of 5 dice!")
    repeat = 'y'
    while repeat.lower() != 'y':
        while True: # Verifies input of greater than one simulation
            n = 100000
            if n > 1: break
            else: continue
        boolean,total = equal_rolls(n)
        if boolean == False: # if there isnt any fivetrue then it returns a zero probability
            print(f"The estimated probability is {float(total)}")
        if boolean == True: # if true, then the boolean will retrieve the probability
            prob = total/n
            print(f'The estimated probability is {prob}')

        repeat = input("Would you like to run this simulation again?")

main()