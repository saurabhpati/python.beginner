# global keyword is a way to tell the python interpreter that the variable is a global variable
# and it is intended to change the value in the global scope. If the global keyword is removed then 
# the operation performed will not be reflected into the variable.

myVariable = 5;
print(myVariable);

def incrementVariable():
    global myVariable;
    myVariable = myVariable + 1;
    print(locals().keys());
    print(globals().keys());

incrementVariable();
print(myVariable);