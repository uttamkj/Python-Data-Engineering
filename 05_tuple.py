#A tuple is like a list — but immutable (cannot be changed after creation). Use parentheses ( ) instead of [ ].

'''

List [ ]
✓
Ordered
✓
Can add / remove items
✓
Can change values
✓
Use for data that changes

Tuple ( )
✓
Ordered
✗
Cannot add / remove
✗
Cannot change values
✓
Use for fixed / constant data
'''

# Creating tuples — use round brackets ( ) 
months = ("Jan", "Feb", "Mar", "Apr") 
coordinates = (12.9716, 77.5946) # Bengaluru lat/lon # Indexing works exactly like lists 
print(months[0]) # Jan 
print(months[-1]) # Apr 
print(months[1:3]) # ('Feb', 'Mar') 

# len, in, count all work the same 
print(len(months)) # 4 
print("Jan" in months) # True 

months.count("Jan") # 1 — counts how many times "Jan" appears
months.index("Mar") # 2 — index of first occurrence of "Mar"

# Tuple unpacking — very common in real code 
db_config = ("localhost", 5432, "mydb") # host, port, db name 

host, port, dbname = db_config 

print(host) # localhost 
print(port) # 5432 
print(dbname) # mydb 

# Converting between list and tuple 
my_list = [1, 2, 3] 
my_tuple = tuple(my_list)

# list → tuple 
back = list(my_tuple) 
# tuple → list # This will CRASH — tuples are immutable # months[0] = "January" ← TypeError: 'tuple' does not support item assignment


'''
When to use List vs Tuple in Data Engineering
List — column values, row data, list of file names to process, dynamic data
Tuple — database connection settings, schema definitions, config constants
Tuple — PySpark schema field definitions use tuples internally
Tuple — slightly faster than list because Python knows it won't change
'''