
## Adding Two List Elements Together

number_list = list(input("Enter 3 Number: "))
word_list = list(input("Enter 3 Word Character: "))

print(number_list, word_list)

new_list = []

for i in range(0, len(number_list)):
    new_list.append(number_list[i] + word_list[i])

print(new_list)

# Example
'''
1st list = [123]
2nd list = [abc]

output = ['1a' , '2b', '3c']
'''

