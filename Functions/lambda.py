# Lambda functions have a single statement and cannot contain multiple expressions.
multiply = lambda number1, number2 : number1 * number2;

number1 = int(input('Enter number1:'));
number2 = int(input('Enter number2:'));

print(multiply(number1, number2));