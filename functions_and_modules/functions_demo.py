def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

# Output
# Value inside function: 10
# Value outside function: 20


###################################
### Variable Function Arguments ###
### Python Default Arguments ###
###################################
def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")
greet(name = "Bruce",msg = "How do you do?")  # 2 keyword arguments
greet("Bruce",msg = "How do you do?")  # 1 positional, 1 keyword argument        
# Output
# Hello Kate, Good morning!
# Hello Bruce, How do you do?
# Hello Bruce, How do you do?
# Hello Bruce, How do you do?

#Having a positional argument after keyword arguments will result into errors. For example the function call as follows:
greet(name="Bruce","How do you do?")  #SyntaxError: non-keyword arg after keyword arg

###################################
### Variable Function Arguments ###
### Python Arbitrary Arguments ###
###################################
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
# Output
# Hello Monica
# Hello Luke
# Hello Steve
# Hello John



###################################
### Recursive function ###
###################################
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))	

###################################
### Anonymous function ###
###################################
'''
In Python, anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword, 
in Python anonymous functions are defined using the lambda keyword.

lambda arguments: expression

use lambda functions when we require a nameless function for a short period of time.
'''
# Program to show the use of lambda functions
double = lambda x: x * 2
print(double(5))
# Output: 10

# is nearly the same as
# def double(x):
#    return x * 2

####### Example use with filter()  #####
# Program to filter out only the even items from a list
'''
The function is called with all the items in the list and a new list is returned
 which contains items for which the function evaluats to True.
'''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)
# Output: [4, 6, 8, 12]

####### Example use with map()  ####
'''
The function is called with all the items in the list and a new list is returned
 which contains items returned by that function for each item.
'''
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
# Output: [2, 10, 8, 12, 16, 22, 6, 24]
