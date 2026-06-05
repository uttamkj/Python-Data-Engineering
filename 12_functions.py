# A lambda is a small anonymous function — defined in one line, no def, no name, no return. It takes inputs and returns one expression automatically.

lambda x : x * 2 
# ↑ keyword    ↑ parameter    ↑ expression (auto-returned)

# Regular function
def double(x):
    return x * 2

# Lambda ✅
lambda x: x * 2

# Lambda basics — same result as def, but inline 
double = lambda x: x * 2 
square = lambda x: x ** 2 
add = lambda x, y: x + y 
greet = lambda name: f"Hello {name}" 
is_senior = lambda sal: sal >= 80000 
print(double(5)) 

# 10 print(square(4)) 
# # 16 print(add(10, 20)) 
# # 30 print(greet("Ravi")) 
# # Hello Ravi print(is_senior(91000)) 
# # True print(is_senior(52000)) 
# # False 
# # Lambda with if-else (ternary inside lambda) 
classify = lambda sal: "Senior" if sal>=80000 else "Mid" if sal>=60000 else "Junior"

print(classify(91000)) 
# Senior 

print(classify(67000)) 
# Mid 

print(classify(45000))
# Junior

'''
Lambda rules
✓
One expression only — no multi-line code inside a lambda
✓
The expression is automatically returned — no
return
keyword
✓
Can take any number of parameters:
lambda x,y,z: x+y+z
✗
Cannot use statements like if/else blocks, loops, or assignments inside
'''

'''
Lambda's real power shows up when combined with Python's built-in functions map(), filter(), and sorted(). These three combinations appear constantly in data engineering.

🔶 Data Engineering link: map(lambda) = PySpark's df.withColumn("new", transform_udf(col)). filter(lambda) = PySpark's df.filter(condition). sorted(key=lambda) = PySpark's df.orderBy(). Same logic — different scale.
'''

# =========================================
# DATA
# =========================================

salaries = [75000, 88000, 52000, 91000, 43000]

names = [
    " ravi ",
    "PRIYA",
    " ankit ",
    "NEHA"
]


# =========================================
# MAP
# Apply a function to every item
# =========================================

after_tax = list(
    map(
        lambda s: round(s * 0.80, 2),
        salaries
    )
)

clean_names = list(
    map(
        lambda n: n.strip().title(),
        names
    )
)

print("After Tax Salaries:")
print(after_tax)

print("\nClean Names:")
print(clean_names)


# =========================================
# FILTER
# Keep only matching items
# =========================================

high_sal = list(
    filter(
        lambda s: s > 70000,
        salaries
    )
)

short_name = list(
    filter(
        lambda n: len(n.strip()) <= 4,
        names
    )
)

print("\nHigh Salaries:")
print(high_sal)

print("\nShort Names:")
print(short_name)


# =========================================
# SORTED
# Sort using custom key
# =========================================

employees = [
    {
        "name": "Ravi",
        "salary": 75000,
        "dept": "engineering"
    },
    {
        "name": "Priya",
        "salary": 88000,
        "dept": "data"
    },
    {
        "name": "Ankit",
        "salary": 52000,
        "dept": "sales"
    },
    {
        "name": "Neha",
        "salary": 91000,
        "dept": "engineering"
    }
]


# Sort by salary ascending
by_sal = sorted(
    employees,
    key=lambda e: e["salary"]
)


# Sort by salary descending
top_sal = sorted(
    employees,
    key=lambda e: e["salary"],
    reverse=True
)


# Sort by department then salary
by_dept = sorted(
    employees,
    key=lambda e: (
        e["dept"],
        e["salary"]
    )
)


print("\nTop Earner:")
print(top_sal[0]["name"], "₹", top_sal[0]["salary"])

print("\nSorted By Department + Salary:")

for e in by_dept:
    print(
        f"{e['dept']:15} "
        f"{e['name']:8} "
        f"₹{e['salary']}"
    )

''' 
*************************   OUTPUT **************************************
After Tax Salaries:
[60000.0, 70400.0, 41600.0, 72800.0, 34400.0]

Clean Names:
['Ravi', 'Priya', 'Ankit', 'Neha']

High Salaries:
[75000, 88000, 91000]

Short Names:
['NEHA']

Top Earner:
Neha ₹ 91000

Sorted By Department + Salary:
data            Priya    ₹88000
engineering     Ravi     ₹75000
engineering     Neha     ₹91000
sales           Ankit    ₹52000
'''

numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))

numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x > 3, numbers))

after_tax = [round(s * 0.8, 2) for s in salaries]

high_sal = [s for s in salaries if s > 70000]


'''

Lambda functions are used heavily in PySpark UDFs (User Defined Functions) and pipeline transformations. These patterns come directly from production code.

🔶 Data Engineering link: Pattern 4 — filter → map → sort chained — is exactly PySpark's df.filter(...).withColumn(...).orderBy(...) method chaining. The mental model is identical. {**r, "bonus": ...} is dictionary unpacking — adds a key to a copy of the dict, same as PySpark's withColumn().

'''


# PATTERN 1 — Column transformation with map+lambda raw_salaries = ["75,000", "88,000", " 52000 ", "91,000"] clean_sal = list(map( lambda s: float(s.strip().replace(",","")), raw_salaries )) print(clean_sal) # [75000.0, 88000.0, 52000.0, 91000.0] # PATTERN 2 — Derived column using map+lambda records = [ {"name":"Ravi", "salary":75000}, {"name":"Priya", "salary":88000}, {"name":"Ankit", "salary":52000}, ] # Add bonus column to every record with_bonus = list(map( lambda r: {**r, "bonus": round(r["salary"]*0.1,2)}, records )) for r in with_bonus: print(f"{r['name']:8} salary=₹{r['salary']} bonus=₹{r['bonus']}") # PATTERN 3 — Filter active + high earners employees = [ {"name":"Ravi", "salary":75000, "active":True}, {"name":"Priya", "salary":88000, "active":True}, {"name":"Ankit", "salary":52000, "active":False}, {"name":"Neha", "salary":91000, "active":True}, ] senior_active = list(filter( lambda e: e["active"] and e["salary"] >= 80000, employees )) print("\nSenior active employees:") for e in senior_active: print(f" {e['name']} ₹{e['salary']}") # PATTERN 4 — Pipeline: filter → map → sort (chained) pipeline_result = sorted( map( lambda e: {**e, "band":"Senior" if e["salary"]>=80000 else "Mid"}, filter(lambda e: e["active"], employees) ), key=lambda e: e["salary"], reverse=True ) print("\nActive employees ranked by salary:") for e in pipeline_result: print(f" {e['name']:8} ₹{e['salary']:>8,} [{e['band']}]")


Lambda is a tool — not always the right one. Knowing when to use lambda vs a regular function is what separates readable code from clever code nobody can maintain.

Copy--- ✅ USE LAMBDA — short, inline, used once --- # Good: simple key for sorted() sorted_emps = sorted(employees, key=lambda e: e["salary"]) # Good: quick transformation in map() bonuses = list(map(lambda s: s * 0.1, salaries)) # Good: simple filter condition active = list(filter(lambda e: e["active"], employees)) --- ❌ USE DEF INSTEAD — complex logic, reused, needs docstring --- # Bad: lambda too complex to read process = lambda r: {"id":int(r["id"]),"name":r["name"].strip().title(),"sal":float(r["salary"]),"bonus":round(float(r["salary"])*0.1,2)} # ✅ Much better as a def def process_record(r): """Cast and clean a raw employee record.""" sal = float(r["salary"]) return { "id" : int(r["id"]), "name" : r["name"].strip().title(), "sal" : sal, "bonus": round(sal * 0.1, 2), }
The decision rule — lambda or def?
Lambda
→ fits on one short line + used in one place + no explanation needed
def
→ multi-line logic OR reused in multiple places OR needs a docstring
def
→ always use def for validator and transformer functions in a pipeline
Lambda
→ always use lambda for
sorted(key=...)
and simple
map/filter
✗
Never assign a lambda to a variable and reuse it everywhere — just write a def