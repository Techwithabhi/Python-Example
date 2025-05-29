
## Finding the Minimum Number in a List

import random

numberList = [random.randint(0, 100) for _ in range(7)]
print("List:", numberList)

a = numberList[0]

# Loop through the list to find the maximum
for b in numberList:
    if b < a:
        a = b  # Update 'a' if 'b' is lesser

print("Minimum number:", a)
