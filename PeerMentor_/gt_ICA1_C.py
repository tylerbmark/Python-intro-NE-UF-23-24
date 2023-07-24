# gt_ICA1_C.py
# Create a program to calculate the estimated hours and minutes for a trip
#
#       Inputs : Miles and
#                Miles per hour
#       Output : Hours, and minutes
#
#
# By Gentry Trimble

def main():
    # Print welcome message
    print("Travel Time Calculator")

    # Retrieve Variables in integers
    miles = int(input("Enter miles: "))
    mph = int(input("Enter miles per hour: "))

    # To gather the time in hours
    htime = miles//mph

    # To gather time in minutes
    mtime = int((miles/mph - htime) * 60)

    # Print Outputs
    print('Estimated travel time: ')
    print(f'Hours: {htime}\nMinutes: {mtime}')

main()


