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
