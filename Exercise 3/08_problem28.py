
## Global variable and local variable

x = 5 # global variable 

def f1():
    global x
    x = 15 # global variable updated
    y = 10 # Local variable

    print("x=%d y=%d" %(x,y))

f1()
print(x)
