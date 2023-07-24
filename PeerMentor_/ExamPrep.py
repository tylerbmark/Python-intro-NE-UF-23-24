# This exam prep will go through the various functions of lists, tuples, file I/O and try except statements

'''In general, when writting to a file, reading a file, opening a file
is but a simple command the difficulty lies in how you want to read the file, or more importantly
how you want to write the file, and remembering to have the file update itself
after it's been modified so when you call the file back later it still has what was written
'''

'''Tuples lists, and nested lists will be primarly what will be used when writing into a file, there are other methods
such as dictionaries that are used later in the course but that is not important at the moment.
 What writing the file comes down to is parsing, or rather picking a part the list in
 a way that you want it to appear in the file, or in a way that you want to read it from a file'''


'''lets start off with a basic csv( think an excell spreadsheet) file like we used in ICA5_C'''
import csv
'''now the data'''

places = [['Athens', 'Greece', '7:00 pm'], ['Aberdeen','Scotland','5:00 pm'],['Berlin', 'Germany', '6:00 pm'],
          ['Barcelona','Spain', '6:00 pm'], ['Beijing', 'China','1:00 am'], ['Cairo', 'Egypt','7:00 pm'],
          ['Hong Kong', 'China', '1:00 am']]

'''Alright, so currently there is not a file created for this data so it'll have to be made
this is where the try and except statements come in handy along with multiple functions
'''
'''first a function to write to the file
def write_list_to_csv(places):
    with open('locdata.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(places)
write_list_to_csv(places)
this function is what I used to place the list into the file initially, 
I've commented it out because it is unnecessary for the program to run
'''
def write_in_file(places,filename):
    with open(filename, 'w', newline='') as file:  # this write function is in the case the current file does not exist
        writer = csv.writer(file)
        writer.writerows(places) # this will separate each place by row

'''Now for a function that will check if the file exists, if so read, if not then write'''

def read_file(filename):
    places = []
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                places.append(row)

    except FileNotFoundError: # to create the new file if one is not found
        print(f'Cannot find the file "{filename}"')
        write_in_file(places,filename)
        print(f'Starting a new file "{filename}".... ')
    return places

'''These functions are only to actually access the file itself, not to parse the data'''
'''the next functions will act as tools to manipulate the data and get it into 
a format that is ideal'''

def add_place(places,filename):
    city = input("City: ")
    country = input("Country: ")
    timezone = input("Timezone: ")
    place = []
    place.append(city)
    place.append(country)
    place.append(timezone)
    places.append(place)
    write_in_file(places,filename)
    print(f"{city} was added to location database. \n")
'''Quite like ICA5_B there are a few functions in here that are similar
in the add function you are manipulating the list within the list '''
def common_timezone(places):
    timezones = []
    common_timezones = []
    for place in places:
        timezone = place[2]
        if timezone not in timezones:
            timezones.append(timezone)
            cities_in_timezone = [place[0]]
            for other_place in places:
                if other_place != place and other_place[2] == timezone:
                    cities_in_timezone.append(other_place[0])
            common_timezones.append((timezone, cities_in_timezone))
    for timezone, cities_in_timezone in common_timezones:
        city_list = ', '.join(cities_in_timezone)
        print(f"Cities in {timezone}: {city_list}")
'''This function is a little tricky, but it's an example of data parsing and how you can 
manipulate a list using booleans to get a provided outcome. 
'''

def display(places):
    if len(places) == 0:
        print("There are no locations added!")
    else:
        for i, row in enumerate(places, start=1):
            print(f'{i}. {row[0]}')

'''Simple display enumerate works great since it allows you to iterate over a list/tuple while 
keeping track of the indicies, especially useful if you'll be using the indicies later'''
def list_places(places):
    for i in range(len(places)):
        place = places[i]
        print(f"{str(i+1)}. {place[0]}, {place[1]},\tTimezone: {place[2]}")
    print()
def get_place_num(places):
    try: # checks to see if there is a valid contact number, if not returns -1 to continue loop
        number = int(input("Number: "))
        if number < 1 or number > len(places):
            print("Invalid Contact Number.")
            raise IndexError
        return number
    except ValueError:
        print("Invalid integer.")
        print()
        return -1
    except IndexError: # in the case of the index being out of range
        print()
        return -1
    '''when dealing with indicies, indexerror is a good way to bypass potential errors'''
def remove(places,filename):
    number = get_place_num(places)
    if number != -1:
        place = places.pop(number-1)
        write_in_file(places,filename)
        print(f"The location {place[0]} has been removed from the location database\n")



def display_title(title):
    print(title)
def display_menu(command_menu):
    for i in command_menu:
        print(i)
    print()

def main():
    title = 'Location Timezone Database\n'
    command_menu = ('add - adds new location to database', 'remove - removes location from database',
                    'list - provides list of locations' , ' common - provides list of cities with common timezones',
                    'exit - to exit the database compiler')
    repeat = 'y'  # so program can be used in repetition
    while repeat.lower() == "y":
        filename = input("Enter a filename: ")  # gathers file name
        locdatabase = read_file(filename)  # reads what contacts are provided in file
        display_title(title)
        display_menu(command_menu)
        command = ''
        print()
        while command != exit:  # Simple decision tree building off of contacts.py
            command = input("Command: ")
            if command == 'display':
                display(locdatabase)
            if command == 'add':
                add(locdatabase, filename)
            if command == 'list':
                list_places(locdatabase)
            if command == 'remove':
                remove(locdatabase, filename)
            if command == 'common':
                common_timezone(locdatabase)
            if command == 'exit':
                print()
                print("Thank you! Bye!")
                print()
                break
            if command != 'exit' and command != 'remove' and command != "list" and command != "add" and command != 'display' and command != 'common':
                print()
                print("Invalid Command. Try again")  # input verification, if none of the provided then the loop will reiterate
        repeat = input("Use Contact Manager again (y/n) ? ")
main()
