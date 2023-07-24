#GT_HW3_A.py
import math

# Essentially, for this problem, initialize variables, then functions to retrieve instance variables, use
# greatest common factor to simplify for other functions
# add, subtract multiply, divide functions, the latter of which using keep change flip
# decision matrix for the division and ensuring no zero denominators regardless of function
# this decision matrix will check if division is the case and if so then neither the denominator nor numerator
# can be zero if that is the case then matrix will prompt another imput for rhs
# main function adds a secondary decision matrix to select functions,
# and relies on the decision matrix of zeros to determine whether or not fractions are valid


class Fraction:
    def __init__(self,numerator=0, denominator=1):#Initializes Variables, numerator and denominator
        self.__numerator = numerator
        self.__denominator = denominator
    def get_numerator(self):
        return self.__numerator #Retrieves instance variable
    def get_denominator(self):
        return self.__denominator
    def simplify(self): #Uses math library greatest common factor function to simplify fractions
        gcd = math.gcd(self.__numerator,self.__denominator)
        self.__numerator//=gcd
        self.__denominator//=gcd
    def add(self,rhs): #addition function, multiply numerator of origin function w/ denominator of rhs, and vice versa
        num = (self.__numerator*rhs.get_denominator()) +(rhs.get_numerator() * self.__denominator)
        den = self.__denominator* rhs.get_denominator()
        result = Fraction(num,den) #Turns results back into a fraction
        result.simplify()# Simplifies said fraction
        return result #returns result
    def subtract(self,rhs):
        num = (self.__numerator*rhs.get_denominator()) -(rhs.get_numerator() * self.__denominator)
        den = self.__denominator* rhs.get_denominator()
        result = Fraction(num, den)
        result.simplify()
        return result
    def multiply(self,rhs):
        num = self.__numerator * rhs.get_numerator()
        den = self.__denominator * rhs.get_denominator()
        result = Fraction(num, den)
        result.simplify()
        return result
    def divide(self,rhs):
        if rhs.get_denominator() == 0 or self.__denominator == 0: # To ensure no zeros are entered for the denominator
            print("Cant divide by zero.")
            return None # To prevent crash from a zero entry
        else:
            num = self.__numerator* rhs.get_denominator() # keep change flip
            den = self.__denominator* rhs.get_numerator()
            result = Fraction(num,den) # assembles fraction as defined by class
            result.simplify() # simplifies
            return result
def GetRHS(decision):
# This entire slice of code is to modularize program, and check to ensure no fractions have 0 in denom
    while True:
        try:
            rhs_str = input("Please enter the second fraction (form: a/b) ")
            rhs_num, rhs_den = map(int, rhs_str.split("/"))  # Turns secondary function into list to separate
            if decision != 4:
                if rhs_den == 0:
                    print("Cannot have a zero as the denominator")
                else:
                    return Fraction(rhs_num,rhs_den)
            else: # To ensure division function is not being divided by zeros, secondary check.
                if rhs_den == 0 or rhs_num ==0:
                    print("Cannot divide with zeros")
                else:
                    return Fraction(rhs_num,rhs_den)
        except ValueError:
            print("Invalid Fraction")
def main():
    print("Welcome to the Fraction Calculator!")
    while True:
        try: # This to prevent crash
            frac_str = input("Enter Designated Fraction (Form: a/b)")
            a,b = map(int,frac_str.split("/")) #Turns string into list then splits
            if b == 0:
                print("Cannot have a zero as the denominator")
            else:
                frac = Fraction(a,b)
                break
        except ValueError:
            print("Invalid Fraction")
    while True: #To create a continous while loop for continued operations
        print("General Menu of Operation:\n 1.Add\n2.Subtract\n3.Multiply\n4.Divide\n 5.Quit")
        decision = input("Enter Operation:")
        if decision == "1":
            rhs_frac = GetRHS(1)
            result = frac.add(rhs_frac)
            print(f"{result.get_numerator()}/{result.get_denominator()}") # So the user can see what has been entered
            frac = result
        elif decision =="2": # Same as the first instance using other class mutators
            rhs_frac = GetRHS(2)
            result = frac.subtract(rhs_frac)
            print(f"{result.get_numerator()}/{result.get_denominator()}")
            frac = result
        elif decision == "3":
            rhs_frac = GetRHS(3)
            result = frac.multiply(rhs_frac)
            print(f"{result.get_numerator()}/{result.get_denominator()}")
            frac = result
        elif decision =="4":
            rhs_frac = GetRHS(4)
            result = frac.divide(rhs_frac)
            print(f"{result.get_numerator()}/{result.get_denominator()}")
            frac = result
        elif decision =="5":
            break
        else:
            print("Invalid Choice, please try again.")
    print("Thank you for using the fraction calculator!")







main()
# By G. Alex Trimble