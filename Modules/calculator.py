# Designing a calculator which will get imported in another file to perform certain calculations.
def add(*tupleinput):
    "Adds the given numbers."
    return sum(tupleinput);

def subtract(*tupleinput):
    "Subtracts all numbers from the first number."
    total = tupleinput[0];
    tupleinput = tupleinput[1:];
    for item in tupleinput:
        total -= item;
    return total;

def multiply(*tupleinput):
    "multiplies all given input."
    total = 1;
    for item in tupleinput:
        total *= item;
    return total;

def divide(dividend, divisor):
    "returns dividend/divisor i.e. input1/input2."
    return dividend/divisor;

def raiseToPower(inputValue, power):
    "Returns input raised to the power of power."
    if type(inputValue) != int or type(power) != int:
        return 'Please provide integer inputs';
    return inputValue ** power;