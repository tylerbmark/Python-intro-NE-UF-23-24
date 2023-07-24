#gt_ICA3_B.py
# Feet to meters converter

# Input: Select a conversion, enter value
#       repeat function

# Output: converted value

# By Gentry Trimble
import conversions_ as conversions
# Imports conversion module
help(conversions)# Verifies docstring is acting as it should
def display_title():
    print("Feet and Meters Converter")
    # Title to be called in main

def display_menu():
    print("Conversions Menu:\na. Feet to Meters\nb. Meters to Feet")
    # menu to be called in repeat while loop
def get_valid_selection():
    while True: # Option verification
        option = input("Select a conversion: ")
        if option == "a" or option == "b":
            break # Uses boolean to verify
        else: print("Invalid Selection. Please try again.")
    return option # returns the verified option selected
def main():
    display_title() # calls title
    repeat = "y"
    while repeat.lower() =="y":
        display_menu() # calls menu
        option = get_valid_selection() # verifies selection, grabs option input
        if option == 'a':
            feet = float(input("Enter Feet: "))
            meters = conversions.to_meters(feet) # uses conversion module to gather meters
            print(f"{round(meters,2)} meters")
        if option == "b":
            meters = float(input("Enter Meters: "))
            feet = conversions.to_feet(meters) # uses conversion module to gather feet
            print(f"{round(feet,2)} feet")
        repeat = input("Perform another conversion? (y/n): ") # repeat verification
    print("Thank you! Bye!")
main()

