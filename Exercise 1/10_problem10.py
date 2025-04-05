
## Finding the middle Element in a list


import random

numList = [random.randint(0, 100) for _ in range(7)]
print("List:", numList)

midEllment = int(len(numList)/2)

print("Middle Element:",numList[midEllment])