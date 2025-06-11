
## What is the use of split and join function of String?

s = str(input("Enter a Sentance: "))

# split : To convert string into list of string
s1 = s.split(" ")
print(s1)

print('\n')
gdthdhfh
s2 = s.split('||')
print(s2)

print('\n')

# For reverse the element which data already splited
s3 = s1[:: -1]
print(s3)

print('\n')

# Join : to convert the list again into string 
print(' '.join(s1))
