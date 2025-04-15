## Find if the number is pronic or not. Number which is the product of two consecutive numbers.

n = int(input("Enter a number: "))
fact = 0

for i in range(1, n + 1) :
    if(i* (i + 1 )== n ):
        print(f"{i} X {i + 1} = {n}")
        fact = i

if fact > 0 :
    print("Pronic number")
else:
    print("Not a pronic number")