#gt_ICA6_A.py
# Calculate the monthly payments on a loan and display formatted results
# input: Loan amount, Yearly interest rate, years

# Output: Loan amount, yearly interest rate, years, monthly payment
# by Gentry Trimble
import locale as lc
from decimal import Decimal
lc.setlocale(lc.LC_ALL, 'en_US.UTF-8')
def monthly_payment(loan, interest, years):

    months = years*12
    interest_decimal = Decimal(str(interest)).quantize(Decimal('0.0'))/100
    monthly_interest = interest_decimal/12
    payment = (loan*monthly_interest)/(1- ((1+ monthly_interest)**-months))
    return payment


def gather_inputs():
    loan = Decimal(input('Loan amount: '))
    interest = Decimal(input("Yearly interest rate: "))
    years = int(input("Loan duration in years: "))
    return loan, interest, years

def main():
    print("Monthly Payment Calculator\n")
    while True:

        print("\nDATA ENTRY")
        loan, interest, years = gather_inputs()
        monthly_payment_amount = monthly_payment(loan,interest,years)
        formatted_loan = lc.currency(loan, grouping=True)
        formatted_interest = '{:.1f}%'.format(interest)
        formatted_payment = lc.currency(monthly_payment_amount, grouping=True)
        line = '{:25} {:>15}'
        print("\nFORMATTED RESULTS")
        print(line.format("Loan Amount: ", formatted_loan))
        print(line.format('Yearly Interest Rate:',formatted_interest))
        print(line.format('Years: ',years))
        print(line.format('Monthly Payment: ', formatted_payment, '\n'))
        choice = input("\nCalculate another monthly payment?  (y/n): ")
        if choice.lower() !='y':
            break
    print("Thank you! Bye!")
main()