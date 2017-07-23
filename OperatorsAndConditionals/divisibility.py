# 1. User enter the number which is expected to be an integer.
# 2. Print out whether the number is divisible by 2 and/or by 3.
# 3. example: 8
# 'The number is divisible by 2 and not by 3'.
# 4. example: 9
# 'The number is not divisible by 2 and divisible by 3'

mandatoryString = 'The number is ';
divisibleString = 'divisible by ';
notString = 'not ';
andString = 'and ';

divisibleBy2String = mandatoryString + divisibleString + '2';
notDivisibleBy2String = mandatoryString + notString + divisibleString + '2';
divisibleBy3String = mandatoryString + divisibleString + '3';
notDivisibleBy3String = mandatoryString + notString + divisibleString + '3';


number = input('Enter the number: ');
number = int(number);

modulo2 = number % 2;
modulo3 = number % 3;

if modulo2 == 0 and modulo3 == 0:
    print(divisibleBy2String, andString, divisibleBy3String);
else:
    if modulo2 == 0:
        print(divisibleBy2String, andString, notDivisibleBy3String);
    elif modulo3:
        print(notDivisibleBy2String, andString, divisibleBy3String);
    else: 
        print(notDivisibleBy2String, andString, notDivisibleBy3String);
