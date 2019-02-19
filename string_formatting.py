# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))


mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)



astring = "Hello world!"
print(astring[3:7])  # prints lo w


astring = "Hello world!"
print(astring[3:7:2]) # prints l

astring = "Hello world!"
print(astring[::-1])  # print !dlrow olleH


astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))  


