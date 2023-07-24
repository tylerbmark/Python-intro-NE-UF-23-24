# gt_ICA6_B.py
# program that reads a file and creates a series of emails

import csv
emails = []
first_names = []
def readcsv(csvfile):
    with open(csvfile, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[2].lower()
            emails.append(email)
            first_name = row[0].title()
            first_names.append(first_name)
    return first_names, emails

def read_txt(txtfile):
    with open(txtfile, 'r') as file:
        email_template = file.read()
    return email_template

def merge_files(csvfile,txtfile):
    first_names,emails = readcsv(csvfile)
    email_template = read_txt(txtfile)
    for email,first_name in zip(emails,first_names):
        merged_mail = email_template.format(email=email, first_name=first_name)
        print('==='*20)
        print(merged_mail)
        print()




def main():
    print("\nEmail Creator\n")
    csvfile = 'email.csv'
    txtfile = 'email_template.txt'
    merge_files(csvfile,txtfile)
main()
