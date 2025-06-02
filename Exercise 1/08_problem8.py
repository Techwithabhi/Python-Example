
## Finding the Maximum Number in a list 

import random

numberList = [random.randint(0, 100) for _ in range(5)]
print("List:", numberList)

a = numberList[0]

# Loop through the list to find the maximum
for b in numberList:
    if b > a:
        a = b  # Update 'a' if 'b' is greater

print("Maximum number:", a)
 
