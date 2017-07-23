# Depicts falsey and truthy values in python.

if 0:
    print('0 is truthy.');
else:
    print('0 is falsey');

if 1:
    print('+ve integers are truthy');
else:
    print('+ve integers are falsey');

if -1:
    print('-ve integers are truthy');
else:
    print('-ve integers are falsey');

if '':
    print('Empty string is truthy');
else:
    print('Empty string is falsey');

if ():
    print('Empty tuple is truthy');
else:
    print('Empty tuple is falsey');

if []:
    print('Empty list is truthy');
else:
    print('Empty list is falsey');

if {}:
    print('Empty dictionary is truthy');
else:
    print('Empty dictionary is falsey');

# Output: 
# 0 is falsey
# +ve integers are truthy
# -ve integers are truthy
# Empty string is falsey
# Empty tuple is falsey
# Empty list is falsey
# Empty dictionary is falsey