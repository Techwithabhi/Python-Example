
## List Compression (to create a list in single line)

# List of even numbers

print('EXE - 1')
a1 = [2 * e for e in range (1, 11)]

print(a1)


# To create a list of even numbers from a given list

print('\nEXE - 2')
num_list = [95, 56, 24, 71, 66, 38, 77, 40, 13, 82]
print(f'The actual list is : {num_list}')
b1 = [e for e in num_list if e % 2 == 0]

print(f"The Even list is {b1}")
