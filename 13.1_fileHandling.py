#File handling lets you read and write text and CSV files — the most common data sources a beginner pipeline works with. Always use with open() — it automatically closes the file even if an error occurs.

# ==============================
# WRITE a text file
# ==============================

print("----- Example 1: Write File -----")

with open("employees.txt", "w") as f:
    f.write("id,name,salary,dept\n")
    f.write("101,Ravi Kumar,75000,engineering\n")
    f.write("102,Priya Sharma,88000,data\n")
    f.write("103,Ankit Singh,52000,sales\n")

print("✅ File written")

print()


# ==============================
# READ entire file
# ==============================

print("----- Example 2: Read Entire File -----")

with open("employees.txt", "r") as f:
    content = f.read()

print(content)

# Output:
# id,name,salary,dept
# 101,Ravi Kumar,75000,engineering
# 102,Priya Sharma,88000,data
# 103,Ankit Singh,52000,sales

print()


# ==============================
# READ line by line
# memory-efficient for large files
# ==============================

print("----- Example 3: Parse Records -----")

with open("employees.txt", "r") as f:
    lines = f.readlines()  # list of lines

# Skip header, parse each data row
records = []

for line in lines[1:]:  # skip header row
    parts = line.strip().split(",")

    records.append({
        "id": int(parts[0]),
        "name": parts[1],
        "salary": float(parts[2]),
        "dept": parts[3],
    })

for r in records:
    print(f"[{r['id']}] {r['name']:15} ₹{r['salary']:>8,.0f}")

# Output:
# [101] Ravi Kumar      ₹75,000
# [102] Priya Sharma    ₹88,000
# [103] Ankit Singh     ₹52,000

print()


# ==============================
# APPEND to existing file
# ==============================

print("----- Example 4: Append Data -----")

with open("employees.txt", "a") as f:
    f.write("104,Neha Patel,91000,engineering\n")

print("✅ New row appended")

print()


# ==============================
# Verify appended data
# ==============================

print("----- Example 5: Verify Append -----")

with open("employees.txt", "r") as f:
    print(f.read())

print()


# ==============================
# Safe read with try-except
# always use this in pipelines
# ==============================

print("----- Example 6: Safe Read -----")


def safe_read(filepath):
    try:
        with open(filepath, "r") as f:
            return f.readlines()

    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return []


lines = safe_read("missing_file.csv")  # returns [] — no crash

print("Returned value:", lines)

# Output:
# ❌ File not found: missing_file.csv
# Returned value: []

print()


# ==============================
# Bonus: Read Existing File Safely
# ==============================

print("----- Example 7: Safe Read Success -----")

lines = safe_read("employees.txt")

print(f"Total lines: {len(lines)}")

for line in lines:
    print(line.strip())

print()


# ==============================
# Bonus: Count Employees
# ==============================

print("----- Example 8: Employee Count -----")

employee_count = len(lines) - 1  # subtract header

print(f"Total Employees = {employee_count}")

# Output:
# Total Employees = 4

with open("data.csv", "r") as f:
    for line in f:
        print(line.strip())

f.read()        # Entire file as one string

f.readline()   # One line at a time

f.readlines()  # List containing all lines

'''
"r"
— read (default). File must exist.
"w"
— write. Creates file, overwrites if exists.
"a"
— append. Adds to end without overwriting.
"x"
— create. Fails if file already exists.
✗
Always use
with open()
— never
f = open()
without closing

'''
#JSON is the most common data format in APIs and modern pipelines. Python's built-in json module reads and writes it perfectly — and a JSON object maps directly to a Python dict.

import json

# ==============================
# Python dict → JSON string (serialise)
# ==============================

print("----- Example 1: Dict to JSON String -----")

employee = {
    "id": 101,
    "name": "Ravi Kumar",
    "salary": 75000,
    "skills": ["Python", "SQL", "PySpark"]
}

json_str = json.dumps(employee, indent=2)

print(json_str)

# Output:
# {
#   "id": 101,
#   "name": "Ravi Kumar",
#   "salary": 75000,
#   "skills": [
#     "Python",
#     "SQL",
#     "PySpark"
#   ]
# }

print()


# ==============================
# JSON string → Python dict (deserialise)
# ==============================

print("----- Example 2: JSON String to Dict -----")

parsed = json.loads(json_str)

print(parsed["name"])       # Ravi Kumar
print(parsed["skills"][0])  # Python

# Output:
# Ravi Kumar
# Python

print()


# ==============================
# WRITE list of dicts to JSON file
# ==============================

print("----- Example 3: Write JSON File -----")

employees = [
    {
        "id": 101,
        "name": "Ravi",
        "salary": 75000
    },
    {
        "id": 102,
        "name": "Priya",
        "salary": 88000
    }
]

with open("employees.json", "w") as f:
    json.dump(employees, f, indent=2)

print("✅ employees.json written")

print()


# ==============================
# READ JSON file back into Python
# ==============================

print("----- Example 4: Read JSON File -----")

with open("employees.json", "r") as f:
    loaded = json.load(f)

for emp in loaded:
    print(f"[{emp['id']}] {emp['name']} — ₹{emp['salary']}")

# Output:
# [101] Ravi — ₹75000
# [102] Priya — ₹88000

print()


# ==============================
# Safe JSON read with error handling
# ==============================

print("----- Example 5: Safe JSON Read -----")


def load_json(filepath):
    """
    Load a JSON file safely.
    Returns [] on any error.
    """

    try:
        with open(filepath, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")

    return []


# Missing file example
data = load_json("missing.json")

print("Returned:", data)

# Output:
# ❌ File not found: missing.json
# Returned: []

print()


# ==============================
# Verify safe load works
# ==============================

print("----- Example 6: Successful Load -----")

data = load_json("employees.json")

print(data)

print()


# ==============================
# Bonus: Pretty Print JSON
# ==============================

print("----- Example 7: Pretty JSON -----")

print(json.dumps(data, indent=4))

print()


# ==============================
# Bonus: Convert JSON to Python Objects
# ==============================

print("----- Example 8: Access Values -----")

for emp in data:
    print(
        f"{emp['name']} earns ₹{emp['salary']:,}"
    )

# Output:
# Ravi earns ₹75,000
# Priya earns ₹88,000

print()


# ==============================
# Bonus: Create Invalid JSON File
# ==============================

print("----- Example 9: Invalid JSON Example -----")

with open("bad.json", "w") as f:
    f.write("{ invalid json }")

bad_data = load_json("bad.json")

print("Returned:", bad_data)

# Output:
# ❌ Invalid JSON: ...
# Returned: []

import json

with open("employees.json") as f:
    employees = json.load(f)

for emp in employees:
    print(emp["name"])


'''
json module — 4 functions to remember
json.dumps(obj)
— Python dict/list → JSON string (dumps = dump string)
json.loads(str)
— JSON string → Python dict/list (loads = load string)
json.dump(obj, f)
— Python → write directly to file
json.load(f)
— read from file → Python dict/list


🔶 Data Engineering link: When Spark reads a JSON data lake file, it does exactly json.loads(line) on each line internally. When you configure a Databricks job, the config is a JSON dict. When REST APIs return data, it's JSON. This is the single most important file format in modern data engineering.'''


import json

# ==============================
# PATTERN 1 — Row-level error handling
# (don't crash on bad rows)
# ==============================

print("----- Pattern 1: Safe Row Transform -----")


def safe_transform(raw):
    """
    Transform one row.

    Returns:
        (cleaned_dict, None)
        OR
        (None, error_str)
    """

    try:
        return {
            "id": int(raw["id"]),
            "name": raw["name"].strip().title(),
            "salary": float(raw["salary"]),
        }, None

    except (KeyError, ValueError, TypeError) as e:
        return None, f"{type(e).__name__}: {e}"


rows = [
    {"id": "101", "name": " ravi ", "salary": "75000"},
    {"id": "102", "name": "priya", "salary": "bad"},   # bad salary
    {"id": "103", "name": "ankit", "salary": "88000"},
]

good = []
bad = []

for row in rows:
    result, err = safe_transform(row)

    (good if result else bad).append(
        result or {**row, "error": err}
    )

print(f"✅ Processed: {len(good)}")
print(f"❌ Rejected : {len(bad)}")

print()

print("Good Records:")
for r in good:
    print(r)

print()

print("Bad Records:")
for r in bad:
    print(r)

# Output:
# ✅ Processed: 2
# ❌ Rejected : 1

print()


# ==============================
# PATTERN 2 — Write results
# + error log to separate files
# ==============================

print("----- Pattern 2: Output Files -----")

with open("silver_output.json", "w") as f:
    json.dump(good, f, indent=2)

with open("error_log.json", "w") as f:
    json.dump(bad, f, indent=2)

print("✅ silver_output.json written")
print("✅ error_log.json written")

print()


# ==============================
# Verify generated files
# ==============================

print("----- Verify silver_output.json -----")

with open("silver_output.json") as f:
    print(f.read())

print()

print("----- Verify error_log.json -----")

with open("error_log.json") as f:
    print(f.read())

print()


# ==============================
# PATTERN 3 — Config-driven pipeline
# (read settings from JSON)
# ==============================

print("----- Pattern 3: Config Driven ETL -----")

config = {
    "pipeline_name": "employee_etl",
    "batch_size": 100,
    "valid_depts": [
        "engineering",
        "data",
        "sales"
    ],
    "bonus_rate": 0.10
}

with open("pipeline_config.json", "w") as f:
    json.dump(config, f, indent=2)

with open("pipeline_config.json") as f:
    cfg = json.load(f)

print(
    f"Running: {cfg['pipeline_name']} "
    f"batch={cfg['batch_size']}"
)

print(
    f"Valid depts: {cfg['valid_depts']}"
)

print(
    f"Bonus rate: {cfg['bonus_rate']}"
)

print()


# ==============================
# Example usage of config
# ==============================

print("----- Config Usage Example -----")

salary = 100000

bonus = salary * cfg["bonus_rate"]

print(f"Salary : ₹{salary:,}")
print(f"Bonus  : ₹{bonus:,.0f}")

print()


# ==============================
# Summary Metrics
# ==============================

print("----- Pipeline Summary -----")

print(f"Input Rows     : {len(rows)}")
print(f"Success Rows   : {len(good)}")
print(f"Rejected Rows  : {len(bad)}")

success_rate = len(good) / len(rows) * 100

print(f"Success Rate   : {success_rate:.2f}%")


bad = [
    {
        "id": "102",
        "salary": "bad",
        "error": "ValueError ..."
    }
]

'''🔶 Data Engineering link: Pattern 2 — separate good rows from bad rows into different output files — is exactly the Dead Letter Queue pattern used in every production pipeline. Bad rows go to a quarantine location for manual review; good rows proceed to the Silver layer. Pattern 3 — config-driven pipelines — is how Databricks jobs are configured: a JSON config file controls batch size, paths, and settings, so you never hardcode values.'''
# Day 13 Task — Try-Except + File Handling: Robust ETL Pipeline

import json

# ===== STEP 0: Write raw input file (simulating a source CSV) =====

raw_csv = """id,name,salary,dept
101, ravi kumar ,75000,engineering
102, priya sharma ,88000,data
103, ankit singh ,bad_salary,sales
104,,91000,engineering
105, sneha rao ,67000,marketing
106, raj verma ,62000,data
"""

with open("raw_employees.csv", "w") as f:
    f.write(raw_csv)

print("✅ raw_employees.csv created")


# ===== STEP 1: Config =====

VALID_DEPTS = [
    "engineering",
    "data",
    "sales",
    "hr"
]


# ===== STEP 2: Safe transform function =====

def transform_row(parts, line_num):
    """
    Parse and validate one CSV row.

    Returns:
        (record, None)
        OR
        (None, error)
    """

    try:
        emp_id, name, salary, dept = parts

        if not name.strip():
            raise ValueError("empty name")

        if dept.strip().lower() not in VALID_DEPTS:
            raise ValueError(
                f"invalid dept: {dept.strip()}"
            )

        return {
            "id": int(emp_id),
            "name": name.strip().title(),
            "salary": float(salary),      # raises ValueError for bad_salary
            "dept": dept.strip().lower(),
            "bonus": round(float(salary) * 0.10, 2),
        }, None

    except ValueError as e:
        return None, {
            "line": line_num,
            "raw": parts,
            "error": str(e)
        }


# ===== STEP 3: Read and process =====

silver = []
errors = []

try:
    with open("raw_employees.csv", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines[1:], start=2):
        # skip header, count from line 2

        parts = line.strip().split(",")

        if len(parts) != 4:
            continue

        rec, err = transform_row(parts, i)

        (silver if rec else errors).append(
            rec or err
        )

except FileNotFoundError:
    print("❌ Input file missing — pipeline aborted")
    exit(1)


# ===== STEP 4: Write outputs =====

with open("silver_employees.json", "w") as f:
    json.dump(silver, f, indent=2)

with open("error_log.json", "w") as f:
    json.dump(errors, f, indent=2)


# ===== STEP 5: Report =====

print("\n===== PIPELINE COMPLETE =====")

print(f"✅ Silver rows   : {len(silver)}")
print(f"❌ Rejected rows : {len(errors)}")

print("\n--- Silver Layer ---")

for r in silver:
    print(
        f"[{r['id']}] "
        f"{r['name']:18} "
        f"₹{r['salary']:>8,.0f} "
        f"Bonus: ₹{r['bonus']:>8,.0f}"
    )

print("\n--- Error Log ---")

for e in errors:
    print(
        f"Line {e['line']}: "
        f"{e['error']}"
    )

