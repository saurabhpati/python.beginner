# Use of random library.
# This library is a very good way to test your code with some random number array. 
import random;

numberList = [143, 222, 332, 501]; 

# choice picks a random number from the list.
print(random.choice(numberList));

# randrange here prints a random odd number between 1-100.
# syntax of randrange is randrange(start, stop, step). 
# start is 0 by default. stop is required. step is 1 by default.
print(random.randrange(1, 100, 2));

# This will print a random number between 1 to 100.
print(random.randrange(100));

# Shuffle will shuffle the given list. Gives different output on each run.
pristineSuite = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'];
random.shuffle(pristineSuite);
print('shuffled suite', pristineSuite);

# uniform(x, y) generates a float value >= x and < y