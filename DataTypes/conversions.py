# Explains different data type conversions in python.

number = input('Give a number: ');
number = int(number, 10);
print('Converting to an integer', number);
print('Converting to a floating point', float(number));
print('Converting to a complex number', complex(number, 1));
print('Converting to a character', chr(number));
print('Converting to a hexamidal string', hex(number));
print('Converting to an octal string', oct(number));
print('---number conversions finished---');

character = input('Enter a character: ');
print('Using ord conversion', ord(character));

x = {
    1: 'Unsure if qualifies as an object'
};

print('original object:', x);
print('Converting to an expression string', repr(x));
print('Converting to a list', list(x));
print('Converting to a set', set(x));
print('Converting to a frozen set', frozenset(x));
tupleList = [('key1', 'value1'), ('key2', 'value2')];
print('Original list containing tuples', tupleList);
print('Converting to dictionary', dict(tupleList));
