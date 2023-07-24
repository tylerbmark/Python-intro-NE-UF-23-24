def print_alpha_num(abc_list,num_list):
    for char in abc_list:
        for num in num_list:
            print(char,num)
    return

print_alpha_num(['a','b','c'],[1,2,3])
print(list(reversed(range(1,11))))
num_list = [1,2,3,4,5]
num_list.remove(2)
print(num_list)
my_list = [2, 'apple',3.5]
my_list[1] = 'orange'
print(my_list)
y = 'stuff;thing;junk;'
z = y.split(';')
print(len(z))
print(5 != 6)
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a*b
d = np.dot(a,b)
print(c,d)