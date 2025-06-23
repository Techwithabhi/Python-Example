
## How to use else with loop in python?
'''
Else can be used with if and while loops in python.

After the break statement in the loop the else statement is not executed.

Else statement is only executed when the condition of the loop is False.
'''

print('EXP - 1')

i = 1
while i <= 10:
    print(i, end= " ")
    if i == 5:
        break
    i += 1
else:
    print("You are in else ")
cxfsdgsfwrsdsd
#########################################################################

print('\nEXE - 2')

i = 1
while i <= 10:
    print(i, end=" ")
    if i == 12:
        break
    i += 1
else:
    print("\nYou are in else")

#########################################################################

print('\nEXP - 3')

for i in range(10):
    print(i, end=" ")
    if i == 12:
        break

else:
    print("\nYou are in else")
