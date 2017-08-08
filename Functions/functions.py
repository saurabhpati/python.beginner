# This is a normal function in python which accepts single/multiple arguments.
def printMe(name, age):
    "This method is fairly diminished over print. Its just a wrapper over the latter."
    print('My name is', name, 'and I am', age, 'years old');

# This is a function which accepts all arguments in the form of a tuple.
def printAllOfMe(*tuplevar):
    "This method will print all arguments provided to it."
    print(type(tuplevar));
    for item in tuplevar:
        print(item);

name = input('What is your name?:');
age = input('What is your age?:');

printMe(name, age);
printAllOfMe(name, age);