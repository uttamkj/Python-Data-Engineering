#A list is an ordered collection of items stored in a single variable. Items can be of any type — and you can mix types in one list.
# Creating lists — use square brackets [ ] 
cities = ["Bengaluru", "Hyderabad", "Pune", "Chennai"] 
salaries = [45000, 72000, 88000, 55000, 91000] 
is_active = [True, False, True, True] 

rev_cities = cities[::-1] #reversed copy of list
print(rev_cities)
print()
cities.reverse() #inplace reverse
print(cities)

# Mixed types in one list (allowed but rare in real data) 
record = [101, "Ravi", 75000.5, True] 

# List of lists — like a table of rows!
employees = [ [101, "Ravi", "Engineering", 75000], [102, "Priya", "Data", 88000], [103, "Ankit", "Sales", 52000], ] 

# Basic properties 
print(len(cities)) 
# 4 — number of items 
print(type(cities)) 
# <class 'list'>
print(max(salaries)) # 91000 
print(min(salaries)) # 45000 
print(sum(salaries)) # 351000


cities = ["Bengaluru", "Hyderabad", "Pune", "Chennai"] 
# Positive indexing — from the start 
print(cities[0]) # Bengaluru — first item 
print(cities[1]) # Hyderabad 
print(cities[3]) # Chennai — last item 

# Negative indexing — from the end (very useful!) 
print(cities[-1]) # Chennai — last item 
print(cities[-2]) # Pune 

# Slicing — extract a portion of the list 
print(cities[0:2]) # ['Bengaluru', 'Hyderabad'] 
print(cities[1:]) # ['Hyderabad', 'Pune', 'Chennai'] 
print(cities[:3]) # ['Bengaluru', 'Hyderabad', 'Pune'] 
print(cities[::-1]) # ['Chennai','Pune','Hyderabad','Bengaluru'] — reversed!
 
# Update an item by index 
cities[2] = "Mumbai" 
print(cities) # ['Bengaluru', 'Hyderabad', 'Mumbai', 'Chennai']

# Access item from list of lists (2D) 
employees = [[101,"Ravi",75000],[102,"Priya",88000]] 
print(employees[0][1]) # "Ravi" — row 0, column 1 
print(employees[1][2]) # 88000 — row 1, column 2

'''
.append(x)	Add x to the end	list.append("Delhi")
.insert(i,x)	Add x at position i	list.insert(0,"Delhi")
.remove(x)	Remove first occurrence of x	list.remove("Pune")
.pop(i)	Remove & return item at index i	list.pop(-1)
.sort()	Sort in place (ascending)	list.sort()
.reverse()	Reverse in place	list.reverse()
.count(x)	Count how many times x appears	list.count("Bengaluru")
.index(x)	Find index of first x	list.index("Pune")
.copy()	Make a copy of the list	new = list.copy()
.clear()	Remove all items	list.clear()
'''

# Most important list methods in action 
salaries = [45000, 72000, 88000, 55000] 
# Add items 
salaries.append(91000) 
print(salaries) # [45000, 72000, 88000, 55000, 91000] 
# Remove items 
salaries.remove(45000) 
print(salaries) # [72000, 88000, 55000, 91000] 
# Sort ascending 
salaries.sort() 
print(salaries) # [55000, 72000, 88000, 91000] 
# Sort descending 
salaries.sort(reverse=True) 
print(salaries) # [91000, 88000, 72000, 55000] 
# Combine two lists 
list1 = [1, 2, 3] 
list2 = [4, 5, 6] 
combined = list1 + list2 
print(combined) # [1, 2, 3, 4, 5, 6] 
# Check membership (from Day 4!) 
print(88000 in salaries) # True

# x.extend([100000, 110000])
# x.insert(0, 40000)
# x.append(120000)