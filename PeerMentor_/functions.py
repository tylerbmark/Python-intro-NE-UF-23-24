# Program of mathematical functions to be used in other modules
# The purpose of this program is to show how to ensure a subprogram can be used into another main program
# This program will act as the subprogram with a host of smaller programs that can be used.



# The path of this program is: C:\Users\alext\PycharmProjects\PythonClass UF\PeerMentor_\functions.py
# as you can see \PeerMentor_\ is the file that functions.py belongs to
# any other program in \PeerMentor_\ will be able to use this module

'''Program with a variety of mathematical functions to be used in other programs'''
def add(x: float,y: float)-> float:
    '''takes x and adds it to y'''
    return x + y

def subtract(x: float,y: float)-> float:
    '''takes x and subtracts it by y'''
    return x-y

def divide(x: float,y: float)-> float:
    '''takes x and divides it by y'''
    return x/y

def multiply(x: float,y: float)-> float:
    '''Multiplies x by y'''
    return x*y


def expo(x:float,y:float)-> float:
    '''raises x to the yth power'''
    return x**y

'''This portion of the module is for data analysis'''
def mean(*args: list) -> float:
    '''to find the mean of a list of variables'''
    for i in args:
        total +=i
    return total/len(args)

def sdev(*args: list) -> float:
    for i in args:
        total += (i - mean(args))**2
    return (total/(len(args)-1))**0.5

