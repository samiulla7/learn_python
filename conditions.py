x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")


#The 'is' operator
'''
Unlike the double equals operator "==", the "is" operator does not match the values of the variables, 
but the instances themselves. For example:
'''
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False