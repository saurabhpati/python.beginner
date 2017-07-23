# indicates the use of for loop in python.
# the program takes three fruits from the user adds them to a list and then displays what the user entered in order.

r = range(0, 3);
indexList = list(r);
fruits = [];

for index in indexList:
    fruit = input('Enter a fruit: ');
    fruits.insert(index, fruit);
else:
    print();
    for fruit in fruits:
        print(fruit);
    else:
        print('These were the fruits entered by you.');