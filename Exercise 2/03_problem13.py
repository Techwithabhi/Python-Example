
## Comparing Two String for ANAGRAMS
'''
Example:

"listen" → "silent" (Both contain the same letters in a different order.)
"race" → "care"
'''

str1 = str(input("Enter a Word: "))  # Listen
str2 = str(input("Enter a Word: "))  # Silent

str1 = str1.replace(" ","").upper()
str2 = str2.replace(" ","").upper()

if sorted(str1) == sorted(str2):
    print("True")

else:
    print("False")

