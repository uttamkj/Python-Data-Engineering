#A set is an unordered collection of unique items. Its superpower: it automatically removes duplicates — which is one of the most common tasks in data cleaning.

# Creating a set — use curly braces { } 
cities = {"Bengaluru", "Hyderabad", "Pune", "Bengaluru", "Hyderabad"} 
print(cities) # {'Bengaluru', 'Hyderabad', 'Pune'} — duplicates removed! 
# Most powerful use: remove duplicates from a list 
raw_depts = ["Engineering", "Sales", "Engineering", "HR", "Sales", "Data"] 
unique_depts = list(set(raw_depts)) 
print(unique_depts) # ['Data', 'Engineering', 'HR', 'Sales'] — order may vary 

# Add and remove 
skills = {"Python", "SQL", "PySpark"} 
skills.add("Azure") 
skills.discard("SQL") # safe remove — no error if not found 
print(skills) # {'Python', 'PySpark', 'Azure'} 
# Membership check — very fast on sets 
print("Python" in skills) # True 
print(len(skills)) # 3 
# Create empty set — must use set(), NOT {} 
empty = set() # correct 
# empty = {} ← this creates an empty DICT, not a set!

# Sets support mathematical operations — union, intersection, difference. These map directly to SQL JOIN concepts you'll use in PySpark.

your_skills = {"Python", "SQL", "PySpark", "Azure"} 
job_requires = {"SQL", "Azure", "Java", "Scala"}

# UNION — all skills from both (no duplicates) 
print(your_skills | job_requires) # {'Python','SQL','PySpark','Azure','Java','Scala'} 

# INTERSECTION — skills you have AND job needs 
print(your_skills & job_requires) # {'SQL', 'Azure'} — your matching skills 

# DIFFERENCE — skills job needs but you DON'T have (your gap!) 
print(job_requires - your_skills) # {'Java', 'Scala'} — skills you need to learn 

# SYMMETRIC DIFFERENCE — skills in one but not both 
print(your_skills ^ job_requires) # {'Python','PySpark','Java','Scala'} 

# Subset check — do you have ALL required skills? 
print(job_requires.issubset(your_skills)) # False — gaps exist


'''
🔶 Data Engineering link: list(set(column)) is the fastest way to get unique values from a column 
— like SELECT DISTINCT dept FROM employees in SQL.
- In PySpark this becomes df.select("dept").distinct()
— same idea, same purpose.
'''