# Displays the use of arguments passed to a program.
# run this program with hello.py <first argument> <second argument> ...

import sys;

x = sys.argv;
print('Number of arguments', len(x));
print(x);
