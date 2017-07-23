# in and not in are membership operators that check whether something is present in the collection.

list = [1, 2, 3, 4, 5];
a = 20;
b = 10;

if a in list:
    print('a is in the list');
else:
    print('a is not in the list');

if b in list:
    print('b is in the list');
else:
    print('b is not in the list');

a = a/b;
b = b/a;

if a in list:
    print('a just made the list');
else:
    print('a could not make the list');

if b in list:
    print('b just made the list');
else:
    print('b could not make the list');