
## Checking for PALINDROME Using Extended Slicing Technique
'''
Examples:

Words: "madam", "racecar", "level"
Numbers: 121, 1221, 12321

Phrases (ignoring spaces & punctuation): "A man, a plan, a canal, Panama!"
'''

user_input = str(input("Enter a Word: ")) 
# madam, kayak, wow

str1 = user_input.upper()

if str1 == str1[::-1]:
    print("True")

else:
    print("False")

