# elif keyword is used to make the else if statement in python
# Requirement for this example: User gives the amount.
# 1. If amount is less than 1000, discount is 5%
# 2. If amount is less than (or equal to) 5000, discount is 10%
# 3. If amount is more than 5000, discount is 15%

amount = input('Enter the amount: ');
amount = int(amount);

if amount < 1000:
    discount = amount * 0.05;
elif amount <= 5000:
    discount = amount * 0.10;
else:
    discount = amount * 0.15;

print('The total amount to be paid', amount - discount);