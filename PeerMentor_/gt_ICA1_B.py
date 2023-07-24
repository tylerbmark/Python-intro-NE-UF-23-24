# gt_ICA1_B.py
# Create  to create a user’s weekly gross and take-home pay
#  Inputs :  Hours Worked and
#            Hourly Pay Rate
#
#  Outputs:  Gross Pay, Tax Rate
#            Taxed Amount, and
#            Take home pay
#
# By Gentry Trimble

def main():
    # Print welcome message
    print("Pay Check Calculator\n ")
    # Tax rate that can be changed
    tax = 18

    # Gather imputs from users
    worktime = float(input("Hours Worked: "))
    workrate = float(input("Hourly Pay Rate: "))

    # Use equations provided to gather outputs
    gross = workrate*worktime
    taxedamt = gross*(tax/100)
    takehome = gross - taxedamt
    # Print outputs
    print(f'Gross Pay: {round(gross,1)}\nTax Rate: {tax} % \n'
          f'Tax Amount: {round(taxedamt,2)} \nTake home pay {round(takehome,2)}')



main()