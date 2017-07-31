# This program intends to take a string input from the user, enccode it
# and then decode it back to the user.
import base64;

inputString = input('Input your string to encode: ');
b64EncodedString = base64.b64encode(bytearray(inputString, 'UTF-8'));
b64DecodedString = base64.b64decode(b64EncodedString);
print('This is the base 64 encoded string', b64EncodedString)
print('This is base 64 decoded string:', b64DecodedString);

# Apparently the base64encode method in the base64 library requires byte like object as input.
# So, In order to encode a string, we have converted a string to a bytearray and then performed the 
# base 64 encoding. 
