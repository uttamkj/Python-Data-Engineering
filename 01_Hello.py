print("Hello, World!")

# this is a comment, it will not be executed by the Python interpreterṇ
'''
This is a multi-line comment, also known as a docstring. 
It can span multiple lines and is often used to provide documentation for functions, classes, or modules. In this case, 
it is just a comment that will not be executed by the Python interpreter.
'''

"""This is another multi-line comment, also known as a docstring. It can also span multiple lines and is often used for the same purposes as the previous docstring.
In this case, it is just another comment that will not be executed by the Python interpreter."""

#Variables 

x = 20 
y = 20.50
first_name = "Uttam Kumar "
last_name = "Jena"

'''
print(x)
print(first_name)
#print(x+first_name) # this will give an error because we cannot add an integer and a string together
print(first_name + last_name)
'''

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
'''

x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

a = b = c = "Orange"
# print(a)
# print(b)
# print(c)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# print(x)
# print(y)
# print(z)

# print(x,y,z)

x = "awesome"

def myfunc(z ,k):
  print("Python is " + x + z ,k)

myfunc(" and it's amazing!", "!")

myfunc(" and it's amazing!", 10)

import random

print(random.randrange(1, 10))
