#gt_ICA9_B.py
#Use inheritance to allow the user to enter data for customers and employees
# Input: Employee/customer -> data of customer/employee
# output: data of customer/ employee

# by. Gentry Trimble

class Person:
    def __init__(self,first_name = '', last_name = '', email = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def fullName(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    def getEmail(self):
        return self.email
    def display(self):
        return f'Name:  {self.fullName()}\nEmail: {self.getEmail()}'
class Customer(Person):
    def __init__(self,first_name,last_name, email, phone_number):
        super().__init__(first_name,last_name,email)
        self.phone_number = phone_number
    def getNumber(self):
        return self.phone_number
    def display(self):
        return 'CUSTOMER\n'+ super().display() + f'\nNumber: {self.phone_number:>5}'
class Employee(Person):
    def __init__(self,first_name,last_name, email,ssn):
        super().__init__(first_name,last_name,email)
        self.ssn = ssn
    def getSSN(self):
        return self.ssn
    def display(self):
        return 'EMPLOYEE\n' + super().display() + f'\nSSN:   {self.ssn:>5}'
def createPerson():
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email: ")
    return first, last, email
def Verification():
    while True:
        try:
            choice = input("Customer or Employee? (c/e): ")
        except ValueError:
            print("Invalid choice. Try again.")
            continue
        else: return choice
def display(choice):
    print("DATA ENTRY")
    first,last, email = createPerson()
    if choice.lower()[0] =='c':
        number = input("Number:")
        customer = Customer(first,last,email,number)
        print()
        print(customer.display())
    if choice.lower()[0] == 'e':
        SSN = input("SSN:")
        print()
        employee = Employee(first,last,email,SSN)
        print(employee.display())


def main():
    print("Customer/ Employee Data Entry")
    repeat = 'y'
    while repeat.lower()[0] == 'y':

        choice = Verification()
        display(choice)
        repeat = input('Enter more data? (y/n): ')
    print("Thanks for using! Bye.")
main()