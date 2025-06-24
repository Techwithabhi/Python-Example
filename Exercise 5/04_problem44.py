## Extract int type values from a list of heterogeneous element?

l1 = ['abc', 34.56, 32, 3+4j, 'b', 55, 65.7, '90', 180]
print(l1)

l2 = []
for e in l1:
    if type(e) == int:
        l2.append(e)

print(l2)
