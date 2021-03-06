# it is very easy to import from a file which is in the same folder.
import calculator

num1 = int(input('Input number 1:'));
num2 = int(input('Input number 2:'));
num3 = int(input('Input number 3:'));
num4 = int(input('Input number 4:'));

print('Adding all four numbers:', calculator.add(num1, num2, num3, num4));
print('num1-num2-num3-num4:', calculator.subtract(num1, num2, num3, num4));
print('Multiply all four numbers:', calculator.multiply(num1, num2, num3, num4));
print('num4/num1:', calculator.divide(num4, num1));

# In order to import a file from another module, we need to do it by sys.path.insert.
import sys
sys.path.insert(0, '../IterationsAndLoops/')

# This will import complete modules from the generator;
from calculator import raiseToPower
print('3 raised to power 4:', raiseToPower(3, 4));
