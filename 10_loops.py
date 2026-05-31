#A for loop iterates over every item in a sequence — list, tuple, string, dict, set — one by one. Unlike while, you don't manage a counter yourself. Python handles it


# Loop over a list 
cities = ["Bengaluru", "Hyderabad", "Pune"] 
for city in cities: 
    print(f"Hiring in: {city}") 

# Loop over a string — character by character 

for char in "Python": 
    print(char, end=" ") 


text = 'I am uttam kumar jena jena uttam'
#words = list(text.split(" "))
#words = tuple(text.split(" "))
words = set(text.split(" "))
print(words)
for word in words:
  print(word)

for idx, word in enumerate(words,start=1):
  print(f"{idx} : {word}")

# P y t h o n # Loop over a tuple 
config = ("host", 5432, "mydb") 
for item in config: 
    print(item) 


# Loop over a dict — iterates over KEYS by default 
emp = {"name":"Ravi", "salary":75000, "dept":"engineering"} 
for key in emp: 
    print(f"{key}: {emp[key]}") 


# Better: loop over key-value pairs with .items() 
for key, val in emp.items(): 
    print(f"{key:10} → {val}") 

# Loop over a list of dicts — like processing JSON records 
records = [ 
    {"id":101, "name":"Ravi", "salary":75000}, 
    {"id":102, "name":"Priya", "salary":88000}, 
] 
for rec in records: 
    print(f"[{rec['id']}] {rec['name']} — ₹{rec['salary']}")


'''
🔶 Data Engineering link: When Spark processes a DataFrame, under the hood it loops over partitions of rows exactly like this — each row is a dict-like structure. Writing Python for loops first teaches you the mental model that makes DataFrame operations intuitive.
'''
#range() generates a sequence of numbers. It's the most common way to loop a fixed number of times or generate indexes.

# range(stop) — 0 to stop-1 
for i in range(5): 
    print(i, end=" ") 

# 0 1 2 3 4 # range(start, stop) — start to stop-1 
for i in range(1, 6): 
    print(i, end=" ") 

# 1 2 3 4 5 # range(start, stop, step) — with step size 

for i in range(0, 20, 5): 
    print(i, end=" ") 
    
# 0 5 10 15 # Countdown — negative step 
for i in range(5, 0, -1):
    print(i, end=" ") 
    
# 5 4 3 2 1 # Use range to access list by index 

salaries = [75000, 88000, 52000, 91000] 
for i in range(len(salaries)): 
    print(f"Index {i}: ₹{salaries[i]}") 

# Generate batch offsets for pagination 
total = 100 
batch_size = 25 
print("\nBatch offsets:") 
for offset in range(0, total, batch_size): 
    print(f" LIMIT {batch_size} OFFSET {offset}") # LIMIT 25 OFFSET 0 / LIMIT 25 OFFSET 25 / ...


'''

range() — the three signatures
range(5)
→ 0,1,2,3,4    (stop only)
range(1,6)
→ 1,2,3,4,5    (start, stop)
range(0,20,5)
→ 0,5,10,15    (start, stop, step)
✗
range(5) does NOT include 5 — stop is always excluded
The most important thing to absorb from today:
Today's task is not just an exercise. It is a real Bronze → Silver → Gold Medallion pipeline written entirely in Python. Raw strings go in, typed and cleaned records come out, then aggregated summaries are produced. You just built Phase 3 of your learning plan — in miniature, in Python — 2 months before you'll do it in Spark.
When you reach Databricks in Week 13, you will write almost identical logic — just replace the Python for loop with PySpark's df.select() and df.groupBy(). The transformation logic is the same. The scale is different.
Also notice: enumerate in today's task tracks which row number you're on — exactly what Spark's monotonically_increasing_id() does. zip pairs schema column names with values — exactly what StructType schema definition does. These aren't coincidences. Python's patterns were the inspiration for the big data tools.
'''

#wo built-in functions that make for loops dramatically more powerful — used constantly in data pipelines.

# -----------------------------
# ENUMERATE — gives index AND value together
# -----------------------------

files = ["jan.csv", "feb.csv", "mar.csv"]

# Without enumerate — clunky
for i in range(len(files)):
    print(f"{i}: {files[i]}")

print("\n------------------\n")

# With enumerate — clean and Pythonic
for idx, file in enumerate(files):
    print(f"File {idx + 1} of {len(files)}: {file}")

print("\n------------------\n")

# Start counting from 1 instead of 0
for idx, file in enumerate(files, start=1):
    print(f"Processing file {idx}: {file}")

print("\n=============================\n")


# -----------------------------
# ZIP — loop over two lists in parallel
# -----------------------------

columns = ["id", "name", "salary", "dept"]
values = [101, "Ravi", 75000, "engineering"]

# Pair them up — like building a dict from two lists
for col, val in zip(columns, values):
    print(f"{col:10}: {val}")

print("\n------------------\n")

# Build a dictionary from two lists using zip
record = dict(zip(columns, values))

print("Dictionary Output:")
print(record)

print("\n=============================\n")


# -----------------------------
# Compare two datasets side by side
# -----------------------------

expected = [100, 200, 300]
actual = [100, 205, 300]

for i, (exp, act) in enumerate(zip(expected, actual), start=1):
    match = "✅" if exp == act else "❌"
    print(f"Row {i}: expected={exp}, actual={act} {match}")

'''
0: jan.csv
1: feb.csv
2: mar.csv

File 1 of 3: jan.csv
File 2 of 3: feb.csv
File 3 of 3: mar.csv

Processing file 1: jan.csv
Processing file 2: feb.csv
Processing file 3: mar.csv

id        : 101
name      : Ravi
salary    : 75000
dept      : engineering

Dictionary Output:
{'id': 101, 'name': 'Ravi', 'salary': 75000, 'dept': 'engineering'}

Row 1: expected=100, actual=100 ✅
Row 2: expected=200, actual=205 ❌
Row 3: expected=300, actual=300 ✅ 

🔶 Data Engineering link: zip(columns, values) is exactly how you build a schema-aware record from raw data. In PySpark, zip with column names is used to create Row objects and build DataFrames dynamically. The expected vs actual pattern is a data reconciliation check — a core data quality task.
 '''

# ==================================================
# LIST COMPREHENSION
# SYNTAX:
# [expression for item in iterable if condition]
#
# expression → what to do
# item       → loop variable
# iterable   → collection
# condition  → optional filter
# ==================================================


# -----------------------------
# 1. Transform every item
# -----------------------------

salaries = [75000, 88000, 52000, 91000, 43000]

after_tax = [round(s * 0.8, 2) for s in salaries]

print(after_tax)

# OUTPUT:
# [60000.0, 70400.0, 41600.0, 72800.0, 34400.0]


print("\n-------------------\n")


# -----------------------------
# 2. Filter items
# -----------------------------

high_sal = [s for s in salaries if s > 70000]

print(high_sal)

# OUTPUT:
# [75000, 88000, 91000]


print("\n-------------------\n")


# -----------------------------
# 3. Transform + Filter
# -----------------------------

senior_tax = [
    round(s * 0.7, 2)
    for s in salaries
    if s > 80000
]

print(senior_tax)

# OUTPUT:
# [61600.0, 63700.0]


print("\n-------------------\n")


# -----------------------------
# 4. Extract columns from list of dicts
# -----------------------------

records = [
    {
        "name": "Ravi",
        "dept": "engineering",
        "salary": 75000
    },
    {
        "name": "Priya",
        "dept": "data",
        "salary": 88000
    },
    {
        "name": "Ankit",
        "dept": "sales",
        "salary": 52000
    }
]

# Extract names
names = [r["name"] for r in records]

# Filter engineering department
eng_names = [
    r["name"]
    for r in records
    if r["dept"] == "engineering"
]

# Extract salary column
all_sal = [r["salary"] for r in records]

print(names)
print(eng_names)
print(f"Avg: ₹{round(sum(all_sal) / len(all_sal), 2)}")

# OUTPUT:
# ['Ravi', 'Priya', 'Ankit']
# ['Ravi']
# Avg: ₹71666.67


print("\n-------------------\n")


# -----------------------------
# 5. String transformation
# -----------------------------

raw_depts = [
    " Engineering ",
    "SALES",
    " Data ",
    "HR"
]

clean_depts = [
    d.strip().lower()
    for d in raw_depts
]

print(clean_depts)

# OUTPUT:
# ['engineering', 'sales', 'data', 'hr']

# Normal loop
result = []
'''
for item in iterable:
    if condition:
        result.append(expression)

# Same using List Comprehension
result = [expression for item in iterable if condition] '''
