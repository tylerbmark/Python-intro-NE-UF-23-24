#gt_ICA8_C.py
# Reads list of customer objects provided by csv
#  allows the user to display data for customer
# INPUT: filename, Customer ID
# OUTPUT: Customer information

# by Gentry Trimble

import csv

class Customer:
    def __init__(self,cust_id,first_name,last_name,company_name,address, city, state, zip):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
    def fullName(self):
        return f"{self.first_name} {self.last_name}"
    def fullAddress(self):
        if self.company_name:
            return f"{self.company_name}\n{self.address}\n{self.city}, {self.state}  {self.zip}"
        else:
            return f"{self.address}\n{self.city}, {self.state}  {self.zip}"



def readcsv(filename):
    customers = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer = Customer(**row)
            customers[customer.cust_id] = customer
    return customers

def find_customer_id(customers,id):
    return customers.get(str(id))

def gatherCSV():
    while True:
        try:
            filename = input('Enter a filename (.csv): ')
            customers = readcsv(filename)
            break
        except FileNotFoundError:
            print("Cannot find the csv file. Try again!")
            continue
    return customers

def main():
    print("Customer Viewer")
    customers = gatherCSV()
    print()
    repeat = 'y'
    while repeat.lower() == 'y':
        while True:
            try:
                ID = input("Enter Customer ID: ")
                customer = find_customer_id(customers,ID)
                if customer:
                    print()
                    print(customer.fullName())
                    print(customer.fullAddress())
                    break
                else:
                    print("No customer with that ID.")
            except ValueError:
                print("No customer with that ID. Invalid Entry")
        print()
        repeat = input("Want to enter another customer ID? (y/n): ")
    print('Thanks for using! Bye!')
main()