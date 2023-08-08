# gt_ICA8_A.py
#Object oriented program that performs calculations on a rectangle

# input: height,width
# output: rectangle, perimeter,area
# by Gentry Trimble

class Rectangle:
    def __init__(self, height , width):
        self.__height = height
        self.__width = width
    def getPerimeter(self):
        return 2*(self.__height + self.__width)
    def getArea(self):
        return self.__height* self.__width
    def getStr(self):
        rectangle_str = ""
        for row in range(self.__height):
            if row == 0 or row == self.__height - 1:
                rectangle_str += "* " * self.__width + "\n"
            else:
                rectangle_str += "*" + " " * 2*(self.__width - 2) +  " * " + "\n"
        return rectangle_str


def main():
    print("Rectangle Calculator")
    repeat = "y"
    while repeat.lower() == 'y':
        height = int(input("Height: \t"))
        width = int(input("Width: \t\t"))
        rectangle = Rectangle(height,width)
        print("Perimeter: ", rectangle.getPerimeter())
        print("Area:  \t   ", rectangle.getArea())
        print(rectangle.getStr())
        repeat = input("Try again ? (y/n): ")
    print("Thank you! Bye!")
main()

