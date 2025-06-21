
## differance between sorted and sort function in python.

# Sorted is a predifined function all the iterables in python, which returns a new list in sorted form.

t1 = (34, 64, 32, 78, 88, 82, 95, 64)
s_t1 = sorted(t1)
print(s_t1)
print(type(s_t1))

#########################################################################

l1 = [34, 64, 32, 78, 88, 82, 95, 64]
l1.sort()
print(l1)           # None
print(type(l1))     # None type

#########################################################################

l1.append(45)
print(l1)
# to add element to list in sorted manner
from sortedcontainers import SortedList
l3 = SortedList(l1)
l3.add(45)
print(l3)
76f68fgiu7g
