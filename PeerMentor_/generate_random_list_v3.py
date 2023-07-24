# File: generate_random_list_v3.py
#   generates a list of lists of random integers (1-10, inclusive)
#   and saves the generated list to a file (bin, csv, or txt)
#
#   Inputs:     two integers (rows and columns)
#   Outputs:    a 2D list of lists (rows*columns) of random integers
#               a file having the 2D list
#   
# by: Kwansun Cho

import random
import csv
import pickle

# define random_list()
def random_list(row, col):
    my_list = []
    for r in range(row):
        r_list = []
        for c in range(col):
            r_list.append(random.randint(1,10))
        my_list.append(r_list)
    print(my_list)
    return my_list

# define get_valid_input()
def get_valid_input(opt):
    while True:
        try:
            option = int(input(f'Enter the number of {opt} (>2): '))
        except ValueError:
            print('Invalid input or no input! Try again!')
            continue
        if option < 3:
            print(f'The number of {opt} must be greater than 2! Try again!')
        else:
            return option

# define get_valid_file_type()
def get_valid_file_type():
    while True:
        file_type = input('Enter a file type (txt, csv, bin): ')

        if file_type == 'bin' or file_type == 'csv' or file_type == 'txt':
            return file_type
        else:
            print('Invalid file type! Try again!')

# define save_list_to_file()        
def save_list_to_file(ftype, my_list):
    rows = len(my_list)
    cols = len(my_list[0])

    filename = f"random_list_{rows}_by_{cols}.{ftype}"

    if ftype == 'bin':
        with open(filename, 'wb') as outfile:
            pickle.dump(my_list, outfile)

    elif ftype == 'csv':
        with open(filename, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(my_list)

    elif ftype == 'txt':
        with open(filename, 'w') as outfile:
            for r in my_list:
                cnt = 0
                for c in r:
                    cnt += 1
                    if cnt == len(r):
                        outfile.write(f'{c}\n')
                    else:
                        outfile.write(f'{c},')

    print(f'Generated random list has been saved in "{filename}"')           

# define main()
def main():
    again = 'y'
    while again.lower() == 'y':
        # welcome message
        print('\nRandom List Generator (version 3)\n')
        
        # get user inputs (row and col)
        rows = get_valid_input("rows")
        cols = get_valid_input("columns")    

        # generate a list of random integers
        new_list = random_list(rows, cols)

        # diplay the generated list
        print(f'Generated List: {new_list}')

        # save the generated list to a file (bin, csv, txt) 
        file_type = get_valid_file_type()
        save_list_to_file(file_type, new_list)
                    
        # ask if the user wants to do it again
        again = input('Generate another list (y/n)? ')

    print('\nThank you! Bye!')

if __name__ == '__main__':
    main()
