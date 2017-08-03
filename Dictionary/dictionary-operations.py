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