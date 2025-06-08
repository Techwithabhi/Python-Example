
## Removing all white spaces in aa string

print('Example 1')

import re

string = 'C O D E'
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", string)
print(result)


print('Example 2')

string = 'A B H I'
string2 = "".join(char for char in string if char != " ")
print(string2)


print('Example 3')

string = 'S A R K A R'
string2 = string.replace(" ", "")
print(string2)
