# '\n' is used to print a new line.
# r'\n' will print \n that means it will escape \n . These strings are called raw strings.
# adding one more \ will escape the escape character to print \n

print(r'\n');
print('\\n');

# %s is used to scan strings while %d is used to scan integers.
print('My Name is %s and my age is %d.' % ('Saurabh', 24));