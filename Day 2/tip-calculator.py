# Tip Calculator
# To find out how much each individual has to pay in a group
# Welcome message
print('Welcome to the tip calculator!')

# Total bill amount
total_bill = input("What's the total bill amount?\n$")

# Percentage of tip you wanna give
tip_amount = input('What percentage tip would you like to give? 10, 12, or 15?\n')
tip_in_percent = int(tip_amount) / 100

# How many's gonna split the bill
people_to_pay = input('How many people to split the bill?\n')

# Computation
bill_per_each = float(total_bill) / int(people_to_pay)
tip_per_each = bill_per_each * tip_in_percent
each_to_pay = "{:.2f}".format(bill_per_each + tip_per_each)

# Amount each person's gonna pay
print(f'Each person should pay: ${each_to_pay}')