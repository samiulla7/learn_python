# # define a list
# my_list = [4, 7, 0, 3]
# # get an iterator using iter()
# my_iter = iter(my_list)

# ## iterate through it using next() 

# #prints 4
# print(next(my_iter))

# #prints 7
# print(next(my_iter))

# ## next(obj) is same as obj.__next__()

# #prints 0
# print(my_iter.__next__())

# #prints 3
# print(my_iter.__next__())

# ## This will raise error, no items left
# next(my_iter)


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        print('in iter method')
        self.n = 0
        return self

    def __next__(self):
        print('in next method')
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
a = PowTwo(4)
i = iter(a)
next(i)
# 1
next(i)
# 2
next(i)
# 4
next(i)
# 8
next(i)
# 16
next(i)
# Traceback (most recent call last):
# ...
# StopIteration



# omparison Between Python Generator vs Iterator
# Let’s see the difference between Iterators and Generators in python.

# In creating a python generator, we use a function. 
# But in creating an iterator in python, we use the iter() and next() functions.
# A generator in python makes use of the ‘yield’ keyword. A python iterator doesn’t.
# Python generator saves the states of the local variables every time ‘yield’ pauses the loop in python. 
# An iterator does not make use of local variables, all it needs is iterable to iterate on.
# A generator may have any number of ‘yield’ statements.
# You can implement your own iterator using a python class; a generator does not need a class in python.
# To write a python generator, you can either use a Python function or a comprehension. 
# But for an iterator, you must use the iter() and next() functions.
# Generator in python let us write fast and compact code. This is an advantage over Python iterators. 
# They are also simpler to code than do custom iterator.
# Python iterator is more memory-efficient. Lest see this with example belo