# gt_ICA9_A.py
# use inheritance to perform calculations on a rectangle or a square as shown in test cases

# input: rectangle/square
#        height, width
#
# output: Perimeter, Area, display

class Rectangle:
    def __init__(self, height=0 , width=0):
        self.__height = height
        self.__width = width
    def setWidth(self,width):
        self.__width = width
    def setHeight(self,height):
        self.__height = height

    def getPerimeter(self):
        return 2*(self.__height + self.__width)
    def getArea(self):
        return self.__height* self.__width
    def __str__(self):
        rectangle_str = ""
        for row in range(self.__height):
            if row == 0 or row == self.__height - 1:
                rectangle_str += "* " * self.__width + "\n"
            else:
                rectangle_str += "*" + " " * 2*(self.__width - 2) +  " * " + "\n"
        return rectangle_str
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)
def inputVerification():
    while True:
        try:
            shape = input("Rectangle or Square? (r/s): ")
        except ValueError:
            print("Invalid Entry. Try again.")
            continue
        else: return shape
def main():
    print("Rectangle Calculator")
    line = '{:12} {:>5}'
    repeat = 'y'
    while repeat.lower()[0] == 'y':
        shape = inputVerification()
        if shape == 'r':
            height = int(input("Height:"))
            width = int(input('Width:'))

            rectangle = Rectangle()
            rectangle.setHeight(height)
            rectangle.setWidth(width)
            print(line.format("Perimeter: ", rectangle.getPerimeter()))
            print(line.format("Area: ", rectangle.getArea()))
            print(rectangle)
        if shape == 's':
            length = int(input("Length: "))
            square = Square(length)
            print(line.format("Perimeter: ", square.getPerimeter()))
            print(line.format("Area: ",square.getArea()))
            print(square)
        repeat = input("Do it again (y/n): ")
    print("Thank you! Bye!")
main()