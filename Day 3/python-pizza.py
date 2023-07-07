# Python Pizza App
print('Welcome to Python Pizza Deliveries!')
print('Small Pizza, S: $15\nMedium Pizza, M: $20\nLarge Pizza, L: $25')
# Taking order
pizza_size = (input('What size pizza do you want? S, M or L?\n')).upper()
want_pepperoni = (input('Do you want pepperoni? Y or N?\n')).upper()
want_extra_cheese = (input('Do you want extra cheese? Y or N?\n')).upper()

# computing bill amount
bill = 0

if pizza_size == 'S':
    bill = 15
    # checking if customer wants pepperoni for small size pizza
    if want_pepperoni == 'Y':
        bill += 2
else:
    if pizza_size == 'M':
        bill = 20
    elif pizza_size == 'L':
        bill = 25
    else:
        print('Pls, select a valid pizza size symbol!')
    # checking if customer wants pepperoni for medium or large size pizza
    if want_pepperoni == 'Y':
        bill += 3
# checking if customer wants extra cheese for small, medium or large size pizza
if want_extra_cheese == 'Y':
    bill += 1

# displaying bill to customer
print(f'Your final bill is: ${bill}.')