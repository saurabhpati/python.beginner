# values can be of any type but keys must be immutable values i.e it means that keys can only be
# strings, numbers or tuples but someting like ['key'] is not allowed to be the key.
fruitDictionary = {
    'king': 'mango',
    'secondInCommand': 'Orange',
    'leutinant': 'apple',
    'sepoy': 'banana',
    'noble': 'pear'
};

# iterating over a dictionary.
for item in fruitDictionary:
    print(item + '-' + fruitDictionary[item]);

# clears all values from the dictionary. Now iterating over the list will not give any entries.
# Note: If given fruitArmy = fruitDictionary, clearing one will clear the other as both will hold 
# the reference to the same value, So using copy which creates a shallow copy of the dictionary.
fruitArmy = fruitDictionary.copy();
fruitArmy.clear()
for item in fruitArmy:
    print(item + '-' + fruitArmy[item]);

# duplicate keys are not maintained in the dictionary, in case a duplicate key is encountered, 
# the last assignment always takes precedence.
fruitDictionary['king'] = 'Watermelon';
print('The winner of the king of the fruits is:', fruitDictionary['king']); #Output: Watermelon

# len gives the total items in the dictionary.
print('Length of fruit dictionary is', len(fruitDictionary)); #Output: 5

# casting to string gives a string representation of the dictionary.
print(str(fruitDictionary));

print(type(fruitDictionary)); #Output: <class 'dict'>
print(type(fruitDictionary['king'])); #Ouput: <class 'str'>

fruitList = ['mango', 'apple', 'banana'];

# fromkeys takes in a list and converts it to a dictionary of keys with value as None.
# the value be set can also be provided, all values will be set to that value.
print(fruitDictionary.fromkeys(fruitList));
# Output: {'mango': None, 'apple': None, 'banana': None}

# This will set the value of all keys to the value provided.
print(fruitDictionary.fromkeys(fruitList, 'sweet'));
# Output: {'mango': 'sweet', 'apple': 'sweet', 'banana': 'sweet'}

# get will return the value of the key, If not found, will return None.
print(fruitDictionary.get('sepoy'));
print(fruitDictionary.get('minister'));

# items will return the list of key value tuple pairs.
print(fruitDictionary.items());
itemList = fruitDictionary.items();

# Item list is a list of tuples with first value being the key and second value being the value.
# item on each iteraton will be the key value pair tuple.
for item in itemList:
    print(item[0] + '--' + item[1]); # item[0] --> key
                                     # item[1] --> value

# update will add the key value pairs in fruitcabinet to fruit dictionary.
# if any key of cabinet is present already in fruit dictionary, then it will not update that 
# key value pair.
fruitCabinet = {
    'Prime': 'Grape',
    'Defence': 'Lemon',
    'Foreign': 'Kiwi'
}
 
fruitDictionary.update(fruitCabinet);
print(fruitDictionary);
# Output: {'king': 'Watermelon', 'secondInCommand': 'Orange', 'leutinant': 'apple', 'sepoy': 'banana', 'noble': 'pear', 'King': 'Mango', 'Pr
# ime': 'Grape', 'Defence': 'Lemon', 'Foreign': 'Kiwi'}

# values will return a list of values.
print(fruitDictionary.values());