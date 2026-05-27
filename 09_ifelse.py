# Basic if statement 
salary = 75000 
if salary > 50000: 
    print("High earner") 
    
# runs because 75000 > 50000
# if-else — two paths
if salary > 80000:
    print("Senior level") 
else: 
    print("Mid level")
    
# this runs — 75000 is not > 80000 
# Condition can be any expression that returns True/False 


# non-empty string = True
name1 = "" 
name = "Uttam" 
if name:
    print(f"Hello {name}") 

data = None 
if data is None: 
    print("Missing value — skip this record")


# elif chain — salary band classifier 

salary = 67000 
if salary >= 100000: 
    band = "Principal" 
elif salary >= 80000:
    band = "Senior" 
elif salary >= 60000: 
    band = "Mid" 
elif salary >= 40000: 
    band = "Junior" 
else: 
    band = "Entry" 
    
print(f"Salary band: {band}") 

# Salary band: Mid # Multiple conditions with and/or 
dept = "engineering" 
experience = 5 
is_active = True 
if dept == "engineering" and experience >= 5 and is_active: 
    print("Eligible for tech lead role") 
elif dept == "engineering" and experience >= 2: 
    print("Eligible for senior engineer")
else: print("Standard engineer track")

# Nested if — check outer condition first, then inner 
is_active = True
salary = 82000 
dept = "engineering" 
if is_active: 
    if salary > 80000: 
        print("Active + high earner") 
    if dept == "engineering": 
        print("→ Flag for promotion review") 
    else: print("Active but below senior threshold") 
else: print("Inactive — skip record") 


# Ternary (one-line) if-else
sal = 9000
status = "Senior" if sal > 80000 else "Junior"
print(status)

# Output:
# Senior


# Real example
employees = [
    {"name": "Ravi", "salary": 75000},
    {"name": "Priya", "salary": 91000},
    {"name": "Ankit", "salary": 48000},
]

for emp in employees:
    label = "High" if emp["salary"] > 80000 else "Standard"
    print(f"{emp['name']:3} → {label}")


# These are the exact if-else patterns you will write in real data engineering pipelines. Study these carefully — you'll recognise them when you get to PySpark.

# =========================================
# PATTERN 1 — Null / Missing Value Check
# =========================================

value = None

if value is None:
    print("NULL — route to dead letter queue")
else:
    print(f"Process value: {value}")


# =========================================
# PATTERN 2 — Data Quality Gate
# =========================================

row = {
    "id": 101,
    "name": "Ravi",
    "salary": -5000,
    "dept": "engineering"
}

valid_depts = ["engineering", "data", "sales", "hr"]

errors = []

# Check negative salary
if row["salary"] < 0:
    errors.append("negative salary")

# Check empty name
if not row["name"].strip():
    errors.append("empty name")

# Check valid department
if row["dept"] not in valid_depts:
    errors.append("invalid department")

# Final validation result
if errors:
    print(f"❌ Row {row['id']} REJECTED: {errors}")
else:
    print(f"✅ Row {row['id']} PASSED quality check")


# =========================================
# PATTERN 3 — Routing Records
# =========================================

record_type = "employee"   # could be contractor, intern, etc.

if record_type == "employee":
    print("→ Write to employees_delta_table")

elif record_type == "contractor":
    print("→ Write to contractors_delta_table")

elif record_type == "intern":
    print("→ Write to interns_delta_table")

else:
    print("→ Write to unknown_records (for review)")


# =========================================
# PATTERN 4 — Derived Column / Tax Calculation
# =========================================

salary = 75000

# Determine tax rate
if salary >= 90000:
    tax_rate = 0.30

elif salary >= 60000:
    tax_rate = 0.20

else:
    tax_rate = 0.10

# Calculate tax
tax = round(salary * tax_rate, 2)

# Calculate net salary
net_salary = salary - tax

print(
    f"Salary: ₹{salary} | "
    f"Tax ({int(tax_rate * 100)}%): ₹{tax} | "
    f"Net: ₹{net_salary}"
)

'''
🔶 Data Engineering link: Pattern 2 (data quality gate) is the Bronze→Silver transformation. In real pipelines you collect all errors per row, then route bad rows to a quarantine table and good rows forward. This exact pattern — collect errors in a list, check if list is non-empty — is used by every senior data engineer.
'''