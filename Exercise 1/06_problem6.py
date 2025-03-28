
## Counting the number of occurances(How many times it comes) of a character in a String

element = str(input("Enter a word: "))

word = element.lower()

character = 'a'

count = 0

# Using for loop 

for i in word:
    if i == character:
        count += 1

print(count)