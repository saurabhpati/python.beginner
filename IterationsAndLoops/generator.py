# The following programs defines a generator, which generates an iterator for all the Fibonacci numbers.

import sys;

numberOfElements = input('Give the number of elements required for fibonacci series: ');

def fibonacci(numberOfElements):
    a, b, counter = 0, 1, 0;

    while counter < numberOfElements:
        yield a;
        a, b = b, a + b;
        counter = counter + 1;

fiboGen = fibonacci(int(numberOfElements));

while True:
    try:
        print(next(fiboGen));
    except StopIteration:
        sys.exit();