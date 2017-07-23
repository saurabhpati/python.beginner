# primitive types such as strings and ints if assigned the same value become one, 
# complex types such as lists are stored in separate location even if they contain the same value.

a = 0; 
b = 0;

print(id(a));
print(id(b));

print(a is b);