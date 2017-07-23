import math;

x = 4;

print('x, the integer', x); 
print('x, the float', float(x));
print('x the complex', complex(x));
print('creating a complex number', complex(x, 4));

y1 = 4.72;

print('absolute value of y1', abs(y1)); 
print('absolute value of y2', abs(-y1));
# abs returns an integer value for integer and float value for floating values.

print('The ceil of y1 is', math.ceil(y1));
print('The ceil of -y1 is', math.ceil(-y1));
print('The floor of y1 is', math.floor(y1));
print('The floor of -y1 is', math.floor(-y1));
print('fabs value of y1', math.fabs(y1)); 
# math.fabs returns a floating point value for all input values.

print('Compare 1 and 2:', (1 > 2) - (1 < 2)); # This gives -1 as output.
print('e raised to the power 1:', math.exp(1)); #2.718
print('ln 2.718:', math.log(2.718)); # ~loge e
print('log10 100:', math.log10(100)); # log10 100 = 2
print('maximum value of 1, 9 and 5:', max(1,9,5));
print('minimum value of 1, 9 and 5:', min(1,9,5));
print('math.modf creates two item tuple of fractional and integer parts:', math.modf(100.712));
print('sqaure root of 1000:', math.sqrt(1000));
