## Globals function

# Globals function returns dictionary
# You can use the globals() function to access or modify global variables
# Within a function or code block.

x = 5 # Global variable

def fun():
    x = 10 # Local variable
    d = globals() # d is dictionary
    # d ['x] = 15 # x is the key in dictionary d which assigns value to global variables

    print("Local x = %d  global x = %d " %(x,d['x']))

fun()
