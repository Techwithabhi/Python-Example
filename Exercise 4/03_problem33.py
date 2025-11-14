
## What are iterators in python?

'''
An iterable is any Python object that can be looped over or iterated. it can be a sequence(e.g., list, tuple, string),
a collection (e.g., set, dictionary), or any object that support iteration.

An iterator used to access the object o0f the iterables one by one by one from 1st element to last element.
An iterator is an object that represents an stream off data. it provides two essential methods: iter() and next()
'''
l1 = [23, 65, 22, 76, 34, 98, 43]
it = iter(l1)

while True:
    try: 
        print(next(it))
    except StopIteration:
        break
        jkzkgcvdsjcvdhkv

    

