#GT_HW3_B.py
#Vector Math!
# I've realized I didn't do psuedocode for this so naturally, let me explain
# The first class, is the 2D version of vectors including just i and j hat,
# for addition and subtraction, it is simply add/subtracting the respective components
# Additional scalar function added for alternative uses later
# The cross product for Vector 2D has two zeros as it uses Vector 3D, sans the k hat vectors
# The 3D vector is essentially a subclass of Vector2D that has an additional variable of khat
# the display operation is what gives the form of the vectors quite like the fraction display in HW3_A
# the display all, takes all the operations and does them all at once while displaying the functions
# that give the answers
# The main function essentially collects all the variables and assembles them into arrays to be used
# using the list map function then indexing to put the variables in their respective positions for
# class usage
# once this happens the display all function can be used
# Naturally I added the ability to either do the 2D or 3D function, this is so this program can be user friendly

class Vector2D:
    def __init__(self,ihat = 0.0,jhat = 0.0): #Initializing variables of Super
        self.ihat = ihat
        self.jhat = jhat
    def __add__(self,rhs):
        return Vector2D(self.ihat + rhs.ihat, self.jhat +rhs.jhat)
    def __sub__(self, rhs):
        return Vector2D(self.ihat - rhs.ihat, self.jhat - rhs.jhat)
    def dot(self,rhs): # useful in other circumstances
        return self.ihat*rhs.ihat + self.jhat*rhs.jhat
    def __mul__(self, scalar):
        return Vector2D(self.ihat*scalar,self.jhat*scalar)
    def CrossProduct(self,rhs):
        return Vector3D(0,0,self.ihat*rhs.jhat - self.jhat*rhs.ihat)
    def magnitude(self): #Useful function for later
        return (self.ihat**2 + self.jhat**2)**0.5
    def Display(self): #simple display
        return f"<{self.ihat},{self.jhat}>"

class Vector3D(Vector2D): # literally vector 2d but with an additional variable, redefining terms
    def __init__(self, ihat = 0.0, jhat = 0.0, khat =0.0):
        super().__init__(ihat,jhat)
        self.khat = khat
    def __add__(self, rhs):
        return  Vector3D(self.ihat + rhs.ihat, self.jhat +rhs.jhat,self.khat +rhs.khat)
    def __sub__(self, rhs):
        return  Vector3D(self.ihat - rhs.ihat, self.jhat - rhs.jhat,self.khat -rhs.khat)
    def dot(self,rhs):
        return self.ihat*rhs.ihat+self.jhat*rhs.jhat+self.khat*rhs.khat
    def CrossProduct(self,rhs):
        return Vector3D(self.jhat*rhs.khat-self.khat*rhs.jhat,
                        -(self.ihat*rhs.khat-self.khat*rhs.ihat),
                            self.ihat*rhs.jhat-self.jhat*rhs.ihat)
    def Display(self): #To display in vector notation
        return f"<{self.ihat},{self.jhat},{self.khat}>"
def DisplayAllOperations(lhs,rhs): # Simple overall display of all operations
    print(f"Executing Operations for {lhs.Display()} and {rhs.Display()}")
    print("---------------------------------")
    print(f"{lhs.Display()} + {rhs.Display()} = {(lhs + rhs).Display()} ")
    print(f"{lhs.Display()} - {rhs.Display()} = {(lhs - rhs).Display()} ")
    print(f"{lhs.Display()} X {rhs.Display()} = {(lhs.CrossProduct(rhs)).Display()}")
    print(f"{lhs.Display()} * {rhs.Display()} = {lhs.dot(rhs)}")
    print("--------------------------------")
def main():
    print("Welcome to the Vector Calculator!")
    decision = input("Would you like to use the 3D function or the 2D function? ")
    if decision == "2D": # Decision matrix to determine whether or not the user wants to do 2d or 3d
        v = input(" Enter the ihat and jhat values for the first 2D vector separated by commas : ")
        vlist = list(map(float,v.split(","))) # Takes in variables as list for inital vector
        ihat = vlist[0] # Assigns class variables
        jhat = vlist[1]
        lhs = Vector2D(ihat,jhat) # becomes vector defined by vector class
        print(f"You've entered: {lhs.Display()}")
        r = input(" Enter the ihat and jhat values for the second 2D vector separated by commas : ")
        rlist = list(map(float,r.split(","))) # takes in numbers of second variable vector
        rihat = rlist[0]
        rjhat = rlist[1]
        rhs = Vector2D(rihat,rjhat)
        print(f"You've entered: {rhs.Display()}")
        DisplayAllOperations(lhs,rhs)
    if decision =="3D": # Essentially the same thing but with an additional khat vector
        v = input(" Enter the ihat, jhat, and khat values for the first 3D vector separated by commas : ")
        vlist = list(map(float, v.split(',')))
        ihat = vlist[0]
        jhat = vlist[1]
        khat = vlist[2]
        lhs = Vector3D(ihat,jhat,khat)
        print(f"You've entered: {lhs.Display()}")
        r = input(" Enter the ihat, jhat, and khat values for the second 3D vector separated by commas : ")
        rlist = list(map(float, r.split(",")))
        rihat = rlist[0]
        rjhat = rlist[1]
        rkhat = rlist[2]
        rhs = Vector3D(rihat,rjhat,rkhat)
        print(f"You've entered: {rhs.Display()}")
        DisplayAllOperations(lhs, rhs)

if __name__ == '__main__':
    main()
# allows for usage in other programs

#by G.Alex Trimble