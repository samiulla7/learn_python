'''Exercise 4: Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element
Expected Output:

Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}'''
from collections import OrderedDict
def get_dict(l):
    d = OrderedDict()
    e = {}
    for i in l:
        if i in d:
            d[i] += 1
            e[i] += 1
        else:
            d[i] = 1
            e[i] = 1
    print("e==",e, "  d==",d)
    return d

print(get_dict([11, 45, 8, 11, 23, 45, 23, 45, 89]))