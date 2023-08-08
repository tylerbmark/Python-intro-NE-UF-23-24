#gt_ICA9_C.py
# use a custom list object to automatically generate and work
# with a series of random integers
# input: # of random integers the list shall have
# output: integers, count, total, average

#by Gentry Trimble

import random

class RandomIntList(list):
    def __init__(self,count):
        for i in range(count):
            random_int = random.randint(1,100)
            self.append(random_int)

    def getCount(self):
        return len(self)

    def total(self):
        return sum(self)
    def average(self):
        return sum(self)/len(self)
    def __str__(self):
        return ', '.join(map(str,self))

    def display(self):
        line = '{:10} {:<5}'
        print(line.format("Integers:", self.__str__()))
        print(line.format("Count:", self.getCount()))
        print(line.format("Average:", self.average()))

def Verify():
    while True:
        try:
            num = int(input("How many random integers should the list have (>0) ?: "))
            if num > 0:
                return num
            if num <=0:
                print("Must enter a positive integer! Try again.")
                raise ValueError
        except ValueError as ve:
            if 'invalid literal' in str(ve):
                print('Invalid input. Try again')



def main():
    repeat = 'y'
    while repeat.lower()[0] == 'y':
        count = Verify()
        random_list = RandomIntList(count)
        random_list.display()
        repeat = input("Do it again? (y/n):")
    print("Thank you! Bye!")
main()

