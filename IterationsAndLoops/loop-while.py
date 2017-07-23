# Indicates the working of the while loop in python.
# The below program prints out the first 10 natural numbers.
 
count = 1;
while count <= 10:
    print(count);
    count = count + 1;

print(); # This is just to add a new line between the outputs of the codes above and below.

# The below program indicates the use of else statement with conditional loop, here
# the else will execute after the conditional expression evaluates to false.
count = 1;
while count <= 10:
    print(count);
    count = count + 1;
else:
    print('increase the limit next time to keep printing natural numbers.');