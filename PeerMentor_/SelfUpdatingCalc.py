# SelfUpdatingCalc.py

# program to use functions.py illustrating the importance of using the correct path

# path of main program: C:\Users\alext\PycharmProjects\PythonClass UF\PeerMentor_\SelfUpdatingCalc.py
# path of functions.py: C:\Users\alext\PycharmProjects\PythonClass UF\PeerMentor_\functions.py
# as you can see, they are both in the PeerMentor_ file so they'll be able to communicate with each other
# If you're having issues with your programs communicating with each other
# 9 times out of 10 its either an import error or a file management issue.
# General tips for file management:
# keep all of your code for a specific project in one place, an easy file name for this class would be COP2273.
# anything you download will be in your downloads file unless you move it over to your designated Python file.
#
# Here is an example, of the communication. Like in ICA3_B and conversions, or ICA4_B and contacts.

# General purpose of this program: an updating calculator with a display

# input: numerical values to compute
# output: computed values on display

# by Gentry Trimble


import functions as funct
import os
def functmenu(function):

    for i in function:
        print(i)
def Printdisplay(display):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+---"*7 + "+")
    count = 0
    for line in display:
        if display[count] != "":
            print("|   " + line + "   ")
        else: print("|\t\t\t\t\t      ")
        count +=1
    print("+--" +"+---"*6 + "-+")



def FunctDisplay(command,x,y):
    if command == 'add':
        return  f'{round(x,3)} + {y} =   {round(funct.add(x,y),3)}', funct.add(x,y)
    if command == 'subtract':
        return f'{round(x,3)} - {y} =    {round(funct.subtract(x,y),3)}', funct.subtract(x,y)
    if command == 'divide':
        return f'{round(x,3)} / {y} =    {round(funct.divide(x,y),3)}', funct.divide(x,y)
    if command == 'multiply':
        return f'{round(x,3)} X {y} =   {round(funct.multiply(x,y),3)}', funct.multiply(x,y)
    if command == 'exponent':
        return f'{round(x,3)} ^ {y} =   {round(funct.expo(x,y),3)}',funct.expo(x,y)
    return "invalid command",None
def InitialVerification():
    while True:
        try:
            x = float(input("Enter your first number: "))
            y = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid or no input. Try again")
            continue
        else:
            return x,y


def inputVerification():
    while True:
        try:
            y = float(input("Enter another number: "))

        except ValueError:
            print('Invalid or no input. Try again.')
            continue
        else:
            return y



def calculator():

    display = ['','','','','','']
    count = 0
    repeat = 'y'
    command = input("Enter function you wish to use:")
    x,y = InitialVerification()
    display[count], x = FunctDisplay(command, x, y)
    Printdisplay(display)
    while count !=5:
        count +=1
        command = input("Enter function you wish to use:")
        y = inputVerification()
        display[count],x = FunctDisplay(command,x,y)
        Printdisplay(display)
        print()
        repeat = input("Would you like to continue? (y/n)")
        if repeat != 'y':
            break
        else: continue

def main():
    print("\nSelf-Updating Calculator\n")
    function = ("add - adds two variables", "subtract- subtracts two variables",
                'divide- divides two variables', 'multiply- multiplies two variables',
                'exponent - raises current value to the new value power')
    functmenu(function)
    print()
    calculator()
    print("Hope this helped!")
main()
