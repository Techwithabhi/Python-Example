
## Implementing variable-length (Average) arguments in Python

print('EXE : 1. [For Tuple]')

import random
lkbnbefrlnfler
def average(*t):
    if len(t) == 0:
        return 0  # Handling empty input
    return sum(t) / len(t)

a = int(input("Enter how many numbers you want for list A: "))
random_numbers1 = tuple(random.randint(1, 100) for _ in range(a))
print(f"The A Tuple elements are: {random_numbers1}")

b = int(input("Enter how many numbers you want for list B: "))
random_numbers2 = tuple(random.randint(1, 100) for _ in range(b))
print(f"The B Tuple elements are: {random_numbers2}")

# Unpacking the tuple using * to pass individual elements as arguments
result1 = average(*random_numbers1)
result2 = average(*random_numbers2)

print('The Average of Tuple A:', result1)
print('The Average of Tuple B:', result2)



print('\nEXE : 2. [For Dictionary]')

def average_with_kwargs (**kwargs):
    values = list(kwargs.values())
    avg = sum(values) / len(values)

    return avg

result_A = {
    "num1": random.randint(1, 100),
    "num2": random.randint(1, 100),
    "num3": random.randint(1, 100),
    "num4": random.randint(1, 100),
    "num5": random.randint(1, 100)
}

print(f"The B Dictionary elements are: {result_A}")

result_B = {
    "value1": random.randint(1, 100),
    "value2": random.randint(1, 100),
    "value3": random.randint(1, 100),
    "value4": random.randint(1, 100),
    "value5": random.randint(1, 100)
}

print(f"The B Dictionary elements are: {result_B}")

result_1 = average_with_kwargs(**result_A)
result_2 = average_with_kwargs(**result_B)

print(f'The averagee is: {result_1}')
print(f'The averagee is: {result_2}')
