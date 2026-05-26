#A dictionary stores data as key: value pairs. Think of it like a real dictionary — you look up a word (key) to get its meaning (value). This is the most important data structure in Python for data engineering.

# Creating a dictionary — use { key: value } 
employee = { "id" : 101, "name" : "Ravi Kumar", "department": "Engineering", "salary" : 75000, "is_active" : True, "skills" : ["Python","SQL", "PySpark"]  } 
# Access values by key 
print(employee["name"]) # Ravi Kumar 
print(employee["salary"]) # 75000 
print(employee["skills"][0]) # Python — access list inside dict 
# Safe access with .get() — returns None if key missing, no crash 
print(employee.get("age")) # None — key doesn't exist 
print(employee.get("age", 0)) # 0 — default value 

# Add and update 
employee["city"] = "Bengaluru" 

# add new key 
# employee["city"] = "Bengaluru" 
employee["salary"] = 82000 
# update existing key 
# Delete a key
del employee["is_active"] 
# Check if key exists 
print("salary" in employee) # True 
print("age" in employee) # False
 
# Nested dict — dict inside a dict (like a JSON object) 
company = { "name" : "TechCorp", "address" : { "city" : "Bengaluru", "pincode": "560001" } } 
print(company["address"]["city"]) # Bengaluru


'''
Method	What it returns	Example
.keys()	All keys	emp.keys()
.values()	All values	emp.values()
.items()	All key-value pairs as tuples	emp.items()
.get(k, d)	Value for key k, or default d	emp.get("age", 0)
.update(d)	Merge another dict in	emp.update({"city":"Bengaluru"})
.pop(k)	Remove key and return its value	emp.pop("salary")
.copy()	Shallow copy of dict	new = emp.copy()


🔶 Data Engineering link: JSON files — the most common data format you'll ingest — are exactly dictionaries. When Spark reads a JSON file, each record becomes a Row object that behaves like a dict. The nested dict above is a nested JSON object — something you'll parse in every real pipeline.
'''
employee = { "id": 101, "name": "Ravi", "dept": "Engineering", "salary": 75000 } 
# Loop over keys 
for key in employee.keys(): 
    print(key) 

# id, name, dept, salary # Loop over values 
for val in employee.values(): 
    print(val) 
    
# 101, Ravi, Engineering, 75000 # Loop over both — most common pattern 
for key, value in employee.items(): 
    print(f"{key}: {value}") 
    
# Merge two dicts (Python 3.9+ uses | operator) 
extra = {"city": "Bengaluru", "experience": 3} 
employee.update(extra) 
print(employee) 
# List of dicts — like a table of JSON records! 
records = [ {"id":101, "name":"Ravi", "salary":75000}, {"id":102, "name":"Priya", "salary":88000}, {"id":103, "name":"Ankit", "salary":52000}, ] # Access like a table 
print(records[1]["name"]) # Priya 
print(records[2]["salary"]) # 52000 
# This is EXACTLY how pandas/pyspark creates DataFrames! # pd.DataFrame(records) ← you'll do this in Week 4



'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered     
'''