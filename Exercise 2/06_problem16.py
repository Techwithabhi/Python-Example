
## Counting Digits, Letters and spaces in a String 
import re

name = 'Python is no 1'

digitcount = re.sub("[^0-9]", "", name)
lettercount = re.sub("[^a-z A-Z]", "", name)
spacecount = re.findall("[ \s]", name)

print(len(digitcount))
print(len(lettercount))
print(len(spacecount))