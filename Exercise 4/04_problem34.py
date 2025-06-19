
## What are generators in Python? Create a generator for first n natural even numbers.

'''
Generators in Python are a type of iterable, like lists or tuples, but they allow you iterate over their elements lazily, one at a time, on-the-fly. This means that generators generate values as you need them, rether than storing all values in memory at once. This can be highly memory-efficient, especially when dealling with large datasets or when generatting an infinite sequence.
'''

def evenNum(n):
    i = 1
    while n :
        yield 2*i
        i += 1
        n -= 1
it = evenNum(10)
even_list = []

while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break

print(even_list)

uyvguguygyigyi
