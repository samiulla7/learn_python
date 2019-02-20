
import example
sum = example.add(4,5.5)
print ('Direct import sum is : %d',sum)


from example import add 
sum = add(4,5.5)
print ('From example import sum is : %d',sum)



import math
print("The value of pi is", math.pi)


# import module by renaming it
import math as m
print("The value of pi is", m.pi)


# import only pi from math module
from math import pi
print("The value of pi is", pi)

# Output: 3.141592653589793
print(math.pi)

# Output: -1.0
print(math.cos(math.pi))

# Output: 22026.465794806718
print(math.exp(10))

# Output: 3.0
print(math.log10(1000))

# Output: 1.1752011936438014
print(math.sinh(1))

# Output: 720
print(math.factorial(6))


'''
While importing a module, Python looks at several places. 
Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path. 
The search is in this order.
The current directory.
PYTHONPATH (an environment variable with a list of directory).
The installation-dependent default directory.
'''
import sys
print (sys.path)
# Output
# ['',
# 'C:\\Python33\\Lib\\idlelib',
# 'C:\\Windows\\system32\\python33.zip',
# 'C:\\Python33\\DLLs',
# 'C:\\Python33\\lib',
# 'C:\\Python33',
# 'C:\\Python33\\lib\\site-packages']

#### The dir() built-in function  ####

'''
We can use the dir() function to find out names that are defined inside a module
'''
dir(example)
# ['__builtins__',
# '__cached__',
# '__doc__',
# '__file__',
# '__initializing__',
# '__loader__',
# '__name__',
# '__package__',
# 'add']

print(example.__name__)
# Output
# 'example'

