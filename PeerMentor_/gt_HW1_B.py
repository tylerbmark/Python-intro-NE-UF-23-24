#gt_HW1_B.py Updated to have a plot of values for grading homeworks
# Program to simulate multiple games of craps and estimate
# probability that player wins
# input: number of games
# output: probability of winning, and games won


# by Gentry Trimble

import random
random.seed(42)
def add(x,y):
    # simple add function for summing dice
    return x+y

def roll():
    # gathers the pair of dice roll
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    return d1,d2
def initialROLL():
    d1,d2 = roll()
    total = add(d1,d2)
    # Takes the initial roll, verifies that the roll was not an immediate loss
    if total == 2 or total == 3 or total == 12:
        return False, 0
    else: return True, total # if not an immediate loss, the value is carried to the game simulation
def oneGame(): # program to simulate one game within the rules of craps
    win = ''
    round = False
    # round is only true when the game is either won or loss according to the rules
    bool_, amount = initialROLL()

    while round == False: # if either of those hasn't occured this will simulate the next rolls
        if amount == 7 or amount == 11:  # checks to see if the initial roll is a win
            win = True
            break
        if bool_ == False:  # or an immediate loss
            win = False
            break
        d1,d2 = roll()
        total = add(d1,d2) # for the proceeding rolls
        if total == amount: # if any of these rolls = the initial roll a win is marked
            round = True
            win = True
            break # and the while loop is broken
        if total ==7: # if the total = 7 before the rolls equal the initial value a loss is marked
            win = False
            round = True
            break
        else: continue

    return win
def printIntro():
    print("Let's simulate a game of Craps!")
def get_simulations():
    while True:
        n = int(input("How many games would you like to simulate? "))
        if n > 1:
            return n
        else: print("Invalid number of simulations, Try again")

def simulate(n):

    wins = 0 # initializing number of wins
    for i in range(n+1): # for loop to run each individual game
        outcome = oneGame()
        if outcome == True:
            wins +=1 # tallies up wins
        else: wins = wins
    print(f"The player wins {wins} games out of {n}!")
    print(f"The estimated probability of a win is {round(((wins/n)*100),3)}%")
    return (wins/n)*100,wins
def main():
    # To put everything together into a simple main()
    printIntro() # gives intro
    repeat = 'y'
    while repeat.lower() == 'y':
        simulate(get_simulations()) # simulates all of the simulations
        repeat = input("Try again (y/n)? ")
    print("Bye!") # final statement




def PlotProb():
    import matplotlib.pyplot as plt
    count = 0
    prob = []

    while count != 10000:

        count +=50
        prob_,_ = simulate(count)
        prob.append(prob_)

    plt.plot(range(100, 10100, 50), prob, label='Probability of Winning')
    plt.axhline(y=49.5, color='r', linestyle='--', label='convergence')
    plt.xlabel('Number of Simulations')
    plt.ylabel('Percentage')
    plt.title('Probability of Winning and Number of Wins in Craps')
    plt.legend()
    plt.grid(True)
    plt.show()
PlotProb()