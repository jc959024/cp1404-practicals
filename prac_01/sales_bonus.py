"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Constants
LOW_SALES_THRESHOLD = 1000
LOW_SALES_BONUS_RATE = 0.1
HIGH_SALES_BONUS_RATE = 0.15

# Input
sales = float(input("Enter sales: $"))

# Calculate bonus
if sales >= 0:
    if sales < LOW_SALES_THRESHOLD:
        bonus = sales * LOW_SALES_BONUS_RATE
    else:
        bonus = sales * HIGH_SALES_BONUS_RATE
    print("Bonus: $", bonus)
else:
    print("Invalid sales amount.")


