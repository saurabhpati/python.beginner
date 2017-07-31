# lstrip strips the string of all the specified characters on the left.
# rstrip strips the string of all the specified characters on the right.
# strip strips the string of all the specified characters.

inputString = '******This is a test string******';
print('lstrip of *: ', inputString.lstrip('*')); 
print('rstrip of *: ', inputString.rstrip('*'));
print('strip of *: ', inputString.strip('*'));

# lower converts all the upper case characters to lower case, similarly
# upper performs the opposite action.
lowercaseInput = inputString.lower();
uppercaseInput = inputString.upper();
print('Lower case of input string: ', inputString.lower());
print('Upper case of input string: ', inputString.upper());

# islower and isupper checks whether alphabets in the string are is lower or us upper.
print('Is input string lower case: ', inputString.islower());
print('Is input string upper case: ', inputString.isupper());
print('Is lower case string lower case: ', lowercaseInput.islower());
print('Is upper case string upper case: ', uppercaseInput.isupper());

# isnumeric, checks whether a string comrises of only numberics.
numericString = '786';
fractionHalfUnicode = '\u00BD'; # 1/2 in vulgar fraction.
toThePower2Unicode = '\u00B2'; # to the power superscript 2.
cornerCaseString = numericString + '!';
print('Is ' + numericString + ' consists of only numerics: ', numericString.isnumeric());
print('Is ' + cornerCaseString + ' consists of only numerics: ', cornerCaseString.isnumeric());
print('Is numericString isdigit', numericString.isdigit());
print('Is numericString isdecimal', numericString.isdecimal());

# isnumeric: if the string contain digits as well as unicode vulgar fractions, subscripts, superscripts,
# roman literals, etc.

# isdigit: if the string contains digits as well as only those unicode strings containing digits 
# like superscript and subscript integers.

# isdecimal: if the string contains pure digits.
print('1/2 unicode string is numeric: ', fractionHalfUnicode.isnumeric());
print('1/2 unicode string is digit: ', fractionHalfUnicode.isdigit());
print('1/2 unicode string is decimal: ', fractionHalfUnicode.isdecimal());
print('to the power 2 unicode string is numeric: ', toThePower2Unicode.isnumeric());
print('to the power 2 unicode string is digit: ', toThePower2Unicode.isdigit());
print('to the power 2 unicode string is decimal: ', toThePower2Unicode.isdecimal());
print('1.0 isnumeric', '1.0'.isnumeric());
print('1.0 isdigit', '1.0'.isdigit());
print('1.0 isdecimal', '1.0'.isdecimal());

# isspace checks whether string consists only of whitespace character(s).
# Empty string does not contain any whitespace, hence isspace is false. 
print('Is input string isspace: ', inputString.isspace()); # 
print('Is 3 whitespaces isspace: ', '   '.isspace()); # Output: True
print('Is empty string isspace: ', ''.isspace()); # Output: False

# The transtab method generates a translation table that maps the characters from input string into a new 
# Output string. i.e. translationTable = str.maketrans('aeiou', '12345'), Now when 
# 'Some random string'.translate(translationTable). 

print(inputString.translate(str.maketrans('aeiou*', '12345-'))); 
# Output: ------Th3s 3s 1 t2st str3ng------

# max prints the maximum character value that is present in the string.
print(max(inputString)); # Output: t as 't' is the character with the maximum value.