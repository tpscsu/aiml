#
# This program take a user input of food price for a meal
# It calculates the tip of 18% and sales tax of 7%
# All these values are printed on the terminal
#

try:
    food_price = float(input('Enter the meal price : '))
    tip = food_price * 0.18
    sales_tax = food_price * 0.07
    total_bill_amount = food_price + tip + sales_tax

    print(f"Food Price: ${food_price: .2f}")
    print(f"Tip: ${tip: .2f}")
    print(f"Sales Tax: ${sales_tax: .2f}")
    print(f"Total Price: ${total_bill_amount: .2f}")
except ValueError:
    print('Invalid input Expected a number')
    exit()
