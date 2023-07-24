#gt_ICA1_A.py
# Create Program to compare unit prices
#   Inputs: price for 64 oz size and
#           price for 32 oz size
#
#   Outputs: price per oz (64 oz) and
#            price per oz (32 oz)
#

# By Gentry Trimble

def main():
    print("Price Comparison\n")

    # Gather inital variables values
    price64 = float(input("Price of 64 oz size: "))
    price32 = float(input("Price of 32 oz size: "))

    # price/ounce to get price per ounce
    PPO64 = price64/64
    PPO32 = price32/32

    # gather the data values of the price per ounce and round it off with the round function
    print("Price per ounce (64 oz):", round(PPO64, 2))
    print("Price per ounce (32 oz):", round(PPO32, 2))

main()

