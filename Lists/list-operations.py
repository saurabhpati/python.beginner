# iterating over a list.

testList = [1, 2, 3] ;

for x in testList:
    print(x, end='\n');

# extend will the given list to the list on which extend is called.
 
languagesKnownList = ['c#', 'javascript','python'];
languagesKnownList.extend(testList)

print('Languages known and extended:', languagesKnownList);

# append will only add a single element to the list at the end of the list.
languagesKnownList.append('C');
print('The good old forgotten friend: ', languagesKnownList);

# pop will remove the last element from the list and return the same.
print('Popped', languagesKnownList.pop());

# index will return the lowest index of the required element.
print('index of javascript is: ', languagesKnownList.index('javascript'));

# insert will add a list at a given index.
languagesKnownList.insert(0, 'C');
print('Good old friend is back at index 0: ', languagesKnownList);

cleansedList = [];

# This loop will try to convert the element in language list into ints, 
# if successful meaning no exceptions were raised, then value of the element is an integer.
# cleansed list will contain only strings. 
# Note: This is done because if the list contains both strings and integers, 
# then using sort method will throw an error.

for language in languagesKnownList:
    try:
        value = int(language);
    except:
        cleansedList.append(language);


cleansedList.sort();
print('Cleansed list: ', cleansedList);