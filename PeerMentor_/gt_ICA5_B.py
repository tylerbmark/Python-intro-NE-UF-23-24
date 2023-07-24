# gt_ICA5_B.py
# File I/O and exception handling of ICA4_B

# Input: File- contacts.csv

# output: write to file
# By Gentry Trimble



import contacts
help(contacts) # shows docstring is working properly and contacts is imported
def display_title(title):
    print(title)
def display_menu(command_menu):
    for i in command_menu:
        print(i)
    print()

def main():
    title = "Contact Manager: Publisher\n"
    command_menu = ("display - Display all contacts",
                    "view - View a contact", "add - Add a contact"
                    , "remove - Remove a contact", "exit - Exit Program")
    repeat = 'y' # so program can be used in repetition
    while repeat.lower() == "y":
        filename  = input("Enter a filename: ") # gathers file name
        contact_list = contacts.read_contacts_from_file(filename) # reads what contacts are provided in file
        display_title(title)
        display_menu(command_menu)
        command = ''
        print()
        while command != exit: # Simple decision tree building off of contacts.py
            command = input("Command: ")
            if command == 'display':
                contacts.display(contact_list)
            if command == 'add':
                contacts.add(contact_list, filename)
            if command == 'view':
                contacts.view(contact_list)
            if command == 'remove':
                contacts.remove(contact_list, filename)
            if command == 'exit':
                print()
                print("Thank you! Bye!")
                print()
                break
            if command != 'exit' and command != 'remove' and command != "view" and command != "add" and command != 'display':
                print()
                print("Invalid Command. Try again") # input verification, if none of the provided then the loop will reiterate
        repeat = input("Use Contact Manager again (y/n) ? ")
main()