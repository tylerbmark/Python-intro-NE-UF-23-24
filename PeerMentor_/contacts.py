# Updated contacts.py

# this iteration of contacts.py includes a file managing system to have
# a place for all contacts to reside
# By Gentry Trimble

'''This module contains functions for managing contacts'''
import csv

def write_contacts_to_file(contacts, filename):
    '''Writes the contacts to a CSV file'''
    with open(filename, 'w', newline='') as file: # this write function is in the case the current file does not exist
        writer = csv.writer(file)
        writer.writerows(contacts)

def read_contacts_from_file(filename):
    '''Reads contacts from a CSV file and returns a 2D list of contacts'''
    contacts = [] # the 2D list of contacts
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError: # to create the new file if one is not found
        print(f'Cannot find the file "{filename}"')
        write_contacts_to_file(contacts,filename)
        print(f'Cannot find the file "{filename}"')
    return contacts

def get_contact_number(contacts):
    '''Asks the user for a contact number and returns a valid contact number or -1
    (for an invalid contact number)'''
    try: # checks to see if there is a valid contact number, if not returns -1 to continue loop
        number = int(input("Number: "))
        if number < 1 or number > len(contacts):
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
def display(contacts):
    '''Displays all contacts'''
    if len(contacts) == 0:
        print("There are no contacts available!")
    else:
        for i, row in enumerate(contacts, start=1):
            print(f'{i}. {row[0]}')

def add(contacts, filename):
    '''Adds a contact'''
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = [name, email, phone]
    contacts.append(contact)
    write_contacts_to_file(contacts, filename)
    print(f'{contact[0]} was added. The file "{filename}" has been updated accordingly.')

def view(contacts):
    '''Views a contact'''
    number = get_contact_number(contacts)
    if number != -1:
        contact = contacts[number - 1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone Number:", contact[2])

def remove(contacts, filename):
    '''Removes a contact'''
    number = get_contact_number(contacts)
    if number != -1:
        contact = contacts.pop(number - 1)
        write_contacts_to_file(contacts, filename)
        print(f'{contact[0]} was removed. The file "{filename}" has been updated accordingly.')
    # removes contact from both file and contacts and updates the file accordingly
