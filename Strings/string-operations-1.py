# This file will explain certain libraries and methods attached to string object to help us
# on working with strings.

# capitalize will make the first Character capital.
welcomeString = 'welcome to this beginner\'s tutorial';
print(welcomeString.capitalize());

# The center method will give a padded string with at least the required characters wide, that means
# if I run 'This'.center(4, 'a'), It will return aThisa, where the first parameter is the required width 
# and the second parameter is the filled character, the default filler is space.
# If the required parameter is less than the length of the string then it will return the string without
# adding any filler.

print(welcomeString.center(40, '\\')); # Ouput: \\welcome to this beginner's tutorial\\\

# The count method will count the number of required instances of input char or string.
# Syntax: input.count('a', start=0, end=len(input)).
# 'a' is the input occurence to count, start by default is zero, indicates the index 
# from where to start counting. End by default is the last index which indicates the index
#  to stop counting.

print(welcomeString.count('i')); # Output: 3
print(welcomeString.count('i', 30, 40)); # Output: 1
print(welcomeString.count('nn')); # Output: 1

# endswith with takes a suffix as input and gives true if the string ends with that suffix otherwise false,
# You can also decide the from where the start and the end of the string should be considered from.

print(welcomeString.endswith('tutorial')); # Output: True
print(welcomeString.endswith('to', 7, 10)); # Output: True

# find determines whether a substring is present inside a string and the string to search can be manipulated
# by start and end parameters as in the above example. This gives the index of the found parameter.
# If not found it returns -1.
print(welcomeString.find('welcome'));  # Output: 0
print(welcomeString.find('to')); # Output: 8
print(welcomeString.find('Halleluiah!')); # Output: -1

# index also does the same, the difference being that index throws a valueError exception when the substring is not found.
# Be careful when index and handle the possible exception cases.
print(welcomeString.index('welcome'));
print(welcomeString.index('to'));

try:
    print(welcomeString.index('Halleluiah!'));
except ValueError:
    print('An exception was raised, the substring was not found.');

# isalnum returns true if there is atleast one alpha numneric string, false otherwise.
alphaNumericString = 'Welcome to this python guide 101'; 

# Output false because string complete string has to be alphanumeric.
# complete string has to be alpha numeric, like abcd123.

print(welcomeString.isalnum());
print('alpha numeric string is alnum', alphaNumericString.isalnum());
print('abcd1 is alphanumberic:', 'abcd1'.isalnum());
print('Whitespace is alphanumeric', ''.isalnum());

# isupper returns true if all alphabetical characters in the string are upper case.
print('All Alphabet Charaters are upper case or not', 'WELCOME TO THIS PYTHON GUIDE 101'.isupper());