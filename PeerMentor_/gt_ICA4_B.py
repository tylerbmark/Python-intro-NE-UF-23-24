# gt_ICA4_B.py
# program to allow user to manage the primary email/phone number for contact
# input: command and input from command
# output: alteration to contact manager
# by. Gentry Trimble

import contacts
help(contacts)
def display_title(title):
    print(f"{title}\n")
def display_menu(command_menu):
    command_menu = ("display - Display all contacts",
          "view - View a contact", "add - Add a contact"
          ,"remove - Remove a contact", "exit - Exit Program")
    for i in command_menu:
        print(i)
    print()

def main():
    contact_list = []
    display_title('')
    display_menu()
    command = ''
    while command != exit: # Simple decision tree building off of contacts.py
        command = input("Command: ")
        if command == 'display':
            contacts.display(contact_list)
        if command == 'add':
            contacts.add(contact_list)
        if command == 'view':
            contacts.view(contact_list)
        if command == 'remove':
            contacts.remove(contact_list)
        if command == 'exit':
            print()
            print("Thank you! Bye!")
            break
        if command != 'exit' and command != 'remove' and command != "view" and command != "add" and command != 'display':
            print("Invalid Command. Try again") # input verification, if none of the provided then the loop will reiterate

if __name__ == '__main__':
    main()