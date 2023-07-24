#gt_ICA7_C.py
# read csv, contains list of FIFA world cup champions
# determines country that has the most,
# INPUT: filename
# OUTPUT: wins, years,
#by Gentry Trimble


import csv
def readcsv(filename):

    dict = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            country = row['Country']
            if country in dict:
                dict[country].append(year)
            else:
                dict[country] = [year]
    return dict

def display(dict):
    sorted_countries = sorted(dict.items(),key=lambda x: x[0])
    print('FIFA World cup Winners\n')
    print(f"{'Country' :<11}  {'Wins': <5}  {'Years'}")
    print(f"{'------':<10}   {'----':<5}  {'-----'}")
    for country, years in sorted_countries:
        wins = len(years)
        years_ = ''
        for i in years:
            if i != len(years):
                years_ += str(i) + ", "
        print(f"{country:<13} {wins:<5} {years_[:-2]}")
def main():
    while True:
        try:
            filename = input("Enter a filename (.csv): ")
            dict = readcsv(filename)
        except FileNotFoundError:
            print("Cannot find the CSV file.Try again!")
        else: break

    display(dict)

main()