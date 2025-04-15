## Different types of parameters in python.

def print_params(x,y,z = 3, *pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)

print_params(1,2,3,5,6,7, foo=1, bar=2)
print_params(1,2)
print_params(1,2,3,'Testing', foo=1, bar=2)