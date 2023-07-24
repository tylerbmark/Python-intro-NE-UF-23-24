# Program to determine where a rocket will be
import math
class kinetic:
    def __init__(self,angle,velocity,height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.ypos = velocity* math.sin(theta)
    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos
    def update(self,time):
        self.xpos = self.xpos + time* self.xvel
        yvel1 = self.yvel -time * 9.8
        self.ypos = self.ypos + time*(self.yvel + yvel1)/2
        self.yvel = yvel1
def getInput():
    a = float(input("Enter Launch angle(Degrees): "))
    v = float(input("Enter launch velocity(meters/sec): "))
    h = float(input("Enter launch height(meters): "))
    t = float(input("Enter time interval between position calc : "))
    return a,v,h,t
def main():
    angle,vel,h0,time = getInput()
    cannon = kinetic(angle,vel,h0)
    while cannon.getY()>=0:
        cannon.update(time)
    print("\nDistance traveled: {0: 0 .if} meters.".format(cball.getXO))
