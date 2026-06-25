# I will pratice the some concepts of *args,**kwargs, dict printing, lambda function, with three major functions (map,filter,reduce)

def exampleOne(*args):
  sum = 0
  for i in args:
    sum+=i
  return sum

print(exampleOne(1,2,3,4,5))


def exampleTwo(**kwargs):
  for key,value in kwargs.items():
    # print(f"key = {key} value = {value}")
    print(f"{key}:{value}")

exampleTwo(name="Uttam", age= 24)


# Valid dictionary with mixed, non-string keys
# Keys in Python dictionaries do not always have to be strings. You can use any data type that is immutable (cannot be changed after creation).
mixed_dict = {
    101: "Employee ID as Integer",  #Numbers
    5.5: "Float Key",               #float
    True: "Boolean Key",            #boolen
    ("IT", "Dev"): "Tuple Key",      #tuple
    "name " : "uttam"
}

print(mixed_dict[101])          # Output: Employee ID as Integer
print(mixed_dict[("IT", "Dev")]) # Output: Tuple Key



employee = {
        "fname": "Raju",
        "lname": "Kumar",
        "age": 44,
        "desc": "HR Manager",
        "dept": "HR",
        "Salary": 100000
    }
# for key,value in employee.items() :
#   print(key, end=':')
#   print(value)


employees = {
    1: {
        "fname": "uttam",
        "lname": "jena",
        "age": 24,
        "desc": "software engineer",
        "dept": "it",
        "Salary": "16 LPA"
    },
    2: {
        "fname": "priya",
        "lname": "sharma",
        "age": 28,
        "desc": "data scientist",
        "dept": "analytics",
        "Salary": "22 LPA"
    },
    3: {
        "fname": "rohit",
        "lname": "verma",
        "age": 31,
        "desc": "product manager",
        "dept": "product",
        "Salary": "25 LPA"
    }
}
for key,value in employees.items():
  print(f'{key} : {value}')

print(employees[1]['fname'])
print('-----------EMPLOYEE LIST---------------')
for key,value in employees.items():
  for i,j in employees[key].items():
    print(f'{i}:{j}')
  print('--------------------------------')

  #Here i can pratice the lambda function

def exampleThree(x):
  return x*x

myFunction = lambda x : x*x

print(myFunction(4))
print(exampleThree(4))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted()
#The map() function applies a function to every item in an iterable:
#The filter() function creates a list of items for which a function returns True:

lst = [1,2,3,4,5]
lst2 = list(map(lambda x:x**2,lst))
print(lst2)
lst4 = list(map(lambda x: x%2 == 0,lst))    
lst3 = list(filter(lambda x: x%2 == 0,lst))    
print(lst3)

from functools import reduce
sum = reduce(lambda x,y:x+y,lst)
print(sum)