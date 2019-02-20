'''
A set is created by placing all the items (elements) inside curly braces {}, 
separated by comma or by using the built-in function set().

It can have any number of items and they may be of different types 
(integer, float, tuple, string etc.). But a set cannot have a mutable element, 
like list, set or dictionary, as its element.
'''
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

############################################################################################

# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)

################################################################################################
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use | operator--------------------A.union(B)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
################################################################################################
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use & operator  ------------ A.intersection(B)
# Output: {4, 5}
print(A & B)
################################################################################################
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use - operator on A ----------------A.difference(B)
# Output: {1, 2, 3}
print(A - B)
################################################################################################
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use ^ operator---------------------------A.symmetric_difference(B)
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)