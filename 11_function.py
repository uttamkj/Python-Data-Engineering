# A function is a named, reusable block of code. You define it once, then call it as many times as you need. Functions are the foundation of clean, maintainable pipelines.

def function_name(parameter1, parameter2):
    #← define + name + inputs    
    """Docstring — describes what this function does"""
    #← optional but good habit    
    # function body     
    return 1
    #← output (optional)

# Define a function — uses the 'def' keyword 
def greet(): 
    print("Hello, Data Engineer!") 

# Call it — use the function name with parentheses 
greet() # Hello, Data Engineer! 
greet() # call again — same output 
greet() # and again — this is the power of reuse 
# Function with a parameter 
def greet_person(name): 
    print(f"Hello, {name}!") 
greet_person("Ravi") 
# Hello, Ravi! greet_person("Priya") # Hello, Priya! # Why functions? Compare these two approaches: # ❌ Without functions — repeated code 
print("Ravi".strip().title()) 
print(" priya ".strip().title()) 
print("ANKIT".strip().title()) 

# ✅ With function — write logic once, use everywhere 
def clean_name(name): 
    return name.strip().title() 

print(clean_name("Ravi")) 
print(clean_name(" priya ")) 
print(clean_name("ANKIT"))

# =========================================
# 1. POSITIONAL ARGUMENTS
# =========================================

def add(a, b):
    return a + b

print("Positional Arguments:")
print(add(10, 5))  # a=10, b=5
print()


# =========================================
# 2. DEFAULT ARGUMENTS
# =========================================

def calculate_bonus(salary, rate=0.10):
    return round(salary * rate, 2)

print("Default Arguments:")
print(calculate_bonus(75000))         # Uses default rate (10%)
print(calculate_bonus(75000, 0.15))   # Overrides default rate
print()


# =========================================
# 3. KEYWORD ARGUMENTS
# =========================================

def create_record(name, dept, salary):
    return {
        "name": name,
        "dept": dept,
        "salary": salary
    }

print("Keyword Arguments:")

rec = create_record(
    salary=75000,
    name="Ravi",
    dept="engineering"
)

print(rec)
print()


# =========================================
# 4. *args
# Accept any number of positional arguments
# =========================================

def total_salary(*salaries):
    return sum(salaries)

print("*args Examples:")

print(total_salary(75000, 88000, 52000))
print(total_salary(75000, 88000, 52000, 91000))
print()


# =========================================
# 5. **kwargs
# Accept any number of keyword arguments
# =========================================

def print_config(**settings):

    for key, value in settings.items():
        print(f"{key}: {value}")

print("**kwargs Example:")

print_config(
    host="localhost",
    port=5432,
    db="mydb",
    timeout=30
)

# def func(a, b):          # Positional
# def func(a=10):          # Default
# func(a=1, b=2)           # Keyword
# def func(*args):         # Multiple positional values -> tuple
# def func(**kwargs):      # Multiple named values -> dict

# =========================================
# 1. Return a Single Value
# =========================================

def clean_salary(raw):
    return float(raw.strip().replace(",", ""))


s = clean_salary(" 75,000 ")

print("Single Return Value:")
print(s)
print()


# =========================================
# 2. Return Multiple Values
# Python actually returns a tuple
# =========================================

def salary_stats(salaries):

    minimum = min(salaries)
    maximum = max(salaries)
    average = round(sum(salaries) / len(salaries), 2)

    return minimum, maximum, average


low, high, avg = salary_stats(
    [75000, 88000, 52000, 91000]
)

print("Multiple Return Values:")
print(f"Min: ₹{low}")
print(f"Max: ₹{high}")
print(f"Avg: ₹{avg}")
print()


# =========================================
# 3. Return Early
# Exit function immediately
# =========================================

def validate_salary(salary):

    if salary is None:
        return False

    if salary < 0:
        return False

    if salary > 10000000:
        return False

    return True


print("Early Return Examples:")
print(validate_salary(75000))
print(validate_salary(-1000))
print(validate_salary(None))
print()


# =========================================
# 4. Return a Dictionary
# Very common in ETL / Data Pipelines
# =========================================

def clean_record(raw):

    return {
        "id": int(raw["id"]),
        "name": raw["name"].strip().title(),
        "salary": float(raw["salary"]),
        "dept": raw["dept"].lower()
    }


raw = {
    "id": "101",
    "name": " ravi ",
    "salary": "75000",
    "dept": "ENGINEERING"
}

print("Dictionary Return:")
print(clean_record(raw))

# =========================================
# 1. LOCAL SCOPE
# Variable exists only inside the function
# =========================================

def process():

    result = "processed"   # local variable

    print(result)


process()

# This would cause an error:
# print(result)

# NameError:
# result is not available outside the function


# =========================================
# 2. GLOBAL SCOPE
# Defined outside functions
# =========================================

BATCH_SIZE = 100   # global constant


def process_batch(records):

    print(f"Batch size: {BATCH_SIZE}")

    return records[:BATCH_SIZE]


sample_records = list(range(1, 201))

batch = process_batch(sample_records)

print(f"Records returned: {len(batch)}")
print()


# =========================================
# 3. Better Approach
# Pass values as parameters
# =========================================

def process_batch_clean(records, batch_size=100):

    return records[:batch_size]


batch = process_batch_clean(sample_records, batch_size=50)

print(f"Clean batch size: {len(batch)}")
print()


# =========================================
# 4. Functions Calling Functions
# Mini Data Pipeline Example
# =========================================

def validate(rec):

    return rec["salary"] > 0 and rec["name"]


def transform(rec):

    rec["name"] = rec["name"].strip().title()

    rec["bonus"] = round(rec["salary"] * 0.10, 2)

    return rec


def run_pipeline(records):

    output = []

    for rec in records:

        if validate(rec):           # call validate()

            output.append(
                transform(rec)      # call transform()
            )

    return output


data = [
    {"name": " ravi ", "salary": 75000},
    {"name": "", "salary": -100},      # filtered out
    {"name": "priya", "salary": 88000},
]

result = run_pipeline(data)

print("Pipeline Output:")

for r in result:
    print(r)

# =========================================
# PATTERN 1 — Validator Function
# Returns True / False
# =========================================

def is_valid_record(rec, valid_depts):
    """
    Return True if record passes all quality checks.
    """

    if not rec.get("name", "").strip():
        return False

    if float(rec.get("salary", -1)) < 0:
        return False

    if rec.get("dept") not in valid_depts:
        return False

    return True


# =========================================
# PATTERN 2 — Transformer Function
# Clean and cast raw data
# =========================================

def transform_record(raw):
    """
    Cast and clean a raw CSV row dictionary.
    """

    salary = float(raw["salary"])

    return {
        "id": int(raw["id"]),
        "name": raw["name"].strip().title(),
        "salary": salary,
        "dept": raw["dept"].lower(),
        "bonus": round(salary * 0.10, 2)
    }


# =========================================
# PATTERN 3 — Aggregator Function
# Create summary statistics
# =========================================

def summarise_dept(records, dept):
    """
    Return salary statistics for a department.
    """

    dept_recs = []

    for record in records:
        if record["dept"] == dept:
            dept_recs.append(record)

    if not dept_recs:
        return None

    salaries = [r["salary"] for r in dept_recs]

    return {
        "dept": dept,
        "headcount": len(dept_recs),
        "avg_salary": round(sum(salaries) / len(salaries), 2),
        "max_salary": max(salaries)
    }


# =========================================
# PATTERN 4 — Pipeline Orchestrator
# validate → transform → split
# =========================================

def run_pipeline(raw_records, valid_depts):
    """
    Full ETL Pipeline
    """

    clean = []
    rejected = []

    for raw in raw_records:

        if is_valid_record(raw, valid_depts):

            clean_record = transform_record(raw)

            clean.append(clean_record)

        else:

            rejected.append(raw)

    return clean, rejected


# =========================================
# INPUT DATA
# =========================================

raw = [
    {
        "id": "101",
        "name": " ravi ",
        "salary": "75000",
        "dept": "engineering"
    },
    {
        "id": "102",
        "name": "",
        "salary": "88000",
        "dept": "data"
    },
    {
        "id": "103",
        "name": " priya ",
        "salary": "88000",
        "dept": "data"
    }
]

depts = [
    "engineering",
    "data",
    "sales"
]


# =========================================
# RUN PIPELINE
# =========================================

clean, rejected = run_pipeline(raw, depts)

print(f"Clean Records: {len(clean)}")
print(f"Rejected Records: {len(rejected)}")

print("\nClean Data:")

for record in clean:
    print(record)

print("\nDepartment Summary:")
print(summarise_dept(clean, "data"))


'''
🔶 Data Engineering link: PySpark functions use all of these — df.write.format("delta").option("path", "...").save() — those chained .option() calls are keyword arguments. Databricks job configs are **kwargs under the hood. Understanding these makes reading Spark docs much easier.

🔶 Data Engineering link: Returning multiple values is how pipeline functions report status — return records_processed, errors_found, duration_seconds. Every production pipeline function returns a result dict or status tuple so the orchestrator knows what happened.

Local variables disappear when the function finishes
✓
Functions can read globals but should not modify them
✓
Pass values in as parameters — makes functions predictable and testable
✗
Avoid
global x
to modify globals inside functions — a bad pattern

🔶 Data Engineering link: Pattern 4 (run_pipeline) is how every production Databricks notebook is structured — separate functions for validate, transform, and aggregate, called by one orchestrator. When you build your Phase 3 project, this is the exact code structure you'll use.
'''