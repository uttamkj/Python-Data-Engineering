# Project: HR Data Pipeline — a complete 4-phase ETL pipeline that reads raw employee data from a CSV, cleans and validates it, analyses it, and writes professional JSON output files. This is your first real GitHub-worthy project.

# Input
# raw_hr_data.csv — 8 employee rows with intentional bad data (missing name, bad salary, wrong dept)

# Bronze layer
# Raw rows read as dicts. No transformation yet — just what the CSV contains.

# Silver layer
# Cleaned, cast, enriched rows. Types are correct. 3 bad rows rejected. Bonus, tax, band added.

# Gold layer
# Summary stats: avg salary, dept breakdown, top earners, band distribution. JSON output files.

# Skills used (tap to explore)
# Variables Dicts Lists Functions Try-Except For loops Lambda map() Casting File I/O JSON Sets


# ------------------------------------------- Phase 1   Config + CSV  ---------------------------------------------------------

import json
from datetime import date
# import os
# print(os.getcwd())

# Pipeline config — single source of truth
CONFIG = {
    "pipeline_name" : "hr_employee_etl",
    "version"       : "1.0",
    "bonus_rate"    : 0.10,
    "batch_size"    : 4,
    "run_date"      : str(date.today()),   # auto: "2026-06-09"
}
VALID_DEPTS = ("engineering", "data", "sales", "hr", "finance")

# Triple-quoted string = multi-line; intentional bad rows mixed in
RAW_CSV = """id,name,salary,dept,experience,active
101,  ravi kumar  ,75000,engineering,4,1
102,  priya sharma  ,88000,data,6,1
103,  ankit singh  ,N/A,sales,2,1       
104,,91000,engineering,7,1              
105,  sneha rao  ,67000,unknown,3,1   
106,  raj verma  ,62000,data,3,1
107,  meera iyer  ,54000,hr,1,1
108,  karan mehta  ,83000,finance,5,0
109,  anjali gupta  ,N/A,hr,4,1
110,  vishal patel  ,72000,engineering,6,1  
111,  neha singh  ,68000,sales,2,1
112,  arjun khanna  ,N/A,unknown,3,0
113,  ritu sharma  ,59000,hr,1,1
114,  amit desai  ,80000,finance,5,1
115,  priya kumar  ,N/A,engineering,4,1
116,  sanjay mehta  ,75000,data,6,1
117,  anjali rao  ,N/A,sales,2,1
"""

with open("raw_hr_data.csv", "w") as f:
    f.write(RAW_CSV)

print(f"✅ Phase 1: created {len(RAW_CSV.strip().splitlines())-1} data rows")

# Why intentional bad data?
# Real-world data is never clean. We put 3 broken rows in so Phase 2 has something to catch and reject. This is how production pipelines work: expect dirty input, validate everything.

# Why date.today() inside CONFIG?
# str(date.today()) converts today's date to a string like "2026-06-09". Storing it in CONFIG means every phase can reference CONFIG["run_date"] without repeating the import.


# ------------------------------------------- Phase 2 Extract + Validate----------------------------------------------------
# Two functions: read_csv() reads the file into a list of row dicts, and validate_row() checks each row for errors. Good rows → valid_rows. Bad rows → rejected_rows.

# dict(zip(headers, parts)) is the classic CSV row-to-dict trick. zip pairs each header with its value; dict() wraps them into a mapping.

# try/except for validation
# We try: float(salary) — if the value is "N/A" Python raises ValueError. Catching it lets us record a clean error message instead of crashing.


# Separation of concerns
# Reading and validating are two different jobs, so they're two separate functions. This makes each easier to test and change independently.





def read_csv(filepath):
    """Returns list of row dicts, or [] on error."""
    try:
        with open(filepath, "r") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        headers = [h.strip() for h in lines[0].split(",")]
        rows = []
        for i, line in enumerate(lines[1:], 2):   # start at line 2
            parts = line.split(",")
            if len(parts) == len(headers):
                row = dict(zip(headers, [p.strip() for p in parts]))
                row["_line"] = i        # track source line for error log
                rows.append(row)
        return rows
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return []

def validate_row(row):
    """Returns list of error strings. Empty list = valid row."""
    errors = []
    if not row.get("name", ""):
        errors.append("empty name")
    try:
        float(row.get("salary", ""))
    except ValueError:
        errors.append(f"bad salary: {row.get('salary')}")
    if row.get("dept", "").lower() not in VALID_DEPTS:
        errors.append(f"invalid dept: {row.get('dept')}")
    return errors

raw_rows = read_csv("raw_hr_data.csv")
valid_rows, rejected_rows = [], []

for row in raw_rows:
    errs = validate_row(row)
    if errs:
        row["_errors"] = errs
        rejected_rows.append(row)
    else:
        valid_rows.append(row)

# print(valid_rows)
print(rejected_rows)

# ✅ Phase 2: 8 rows read | 5 valid | 3 rejected ❌ Line 4: ['bad salary: N/A'] ❌ Line 5: ['empty name'] ❌ Line 6: ['invalid dept: unknown']

# ------------------------------------------- Phase 3  Transform + Enrich-----------------------------------------------


# We take each valid raw row and turn it into a clean, typed, enriched Silver row. Cast strings to ints/floats/bools, clean names, and add 3 derived columns using lambda functions.

# Lambda functions
# lambda s: "Senior" if s >= 80000 else "Mid" if s >= 60000 else "Junior" — a one-liner function stored in a variable. Perfect for simple classification logic.


# map()
# list(map(transform_row, valid_rows)) applies transform_row to every item. Cleaner than writing a for loop + append when the output is 1-to-1 with input.

# Type casting
# int(), float(), bool(int()) — CSV gives you strings for everything. Phase 3's job is converting to the right type so Phase 4 can do math on them.

# Lambda classifiers
get_band     = lambda s: "Senior" if s >= 80000 else "Mid" if s >= 60000 else "Junior"
get_tax_rate = lambda s: 0.30 if s >= 90000 else 0.20 if s >= 60000 else 0.10

def transform_row(raw):
    """Cast, clean, and enrich one valid row → Silver dict."""
    sal  = float(raw["salary"])
    rate = get_tax_rate(sal)
    return {
        "id"         : int(raw["id"]),
        "name"       : raw["name"].strip().title(),   # "  ravi kumar  " → "Ravi Kumar"
        "dept"       : raw["dept"].lower(),
        "salary"     : sal,
        "experience" : int(raw["experience"]),
        "active"     : bool(int(raw["active"])),     # "0"→0→False, "1"→1→True
        "bonus"      : round(sal * CONFIG["bonus_rate"], 2),
        "tax_rate"   : rate,
        "tax_amount" : round(sal * rate, 2),
        "net_salary" : round(sal * (1 - rate), 2),
        "band"       : get_band(sal),
    }

silver = list(map(transform_row, valid_rows))

# ✅ Phase 3: 5 rows transformed to Silver layer [101] Ravi Kumar ₹75,000 Mid net=₹60,000 [102] Priya Sharma ₹88,000 Senior net=₹70,400 [106] Raj Verma ₹62,000 Mid net=₹49,600 [107] Meera Iyer ₹54,000 Junior net=₹48,600 [108] Karan Mehta ₹83,000 Senior net=₹66,400

# Why bool(int(raw["active"])) and not just bool(raw["active"])?
# All CSV values are strings. bool("0") returns True because a non-empty string is truthy! You must convert to int first: int("0") = 0, then bool(0) = False. This is a classic Python gotcha.



# ------------------------------------------- Phase 4   Aggregate + Load (Gold) -----------------------------------------


# Build the Gold summary: overall stats, per-department breakdown, leaderboard, band distribution. Then write 3 JSON output files and print a formatted report. This is where everything comes together

# List comprehensions for stats
# [r["salary"] for r in silver] extracts all salaries in one line. Then sum(), max(), min(), len() give you all the stats you need.


# Sets for unique values
# set(r["dept"] for r in silver) gets unique departments automatically — no duplicates. Wrap in sorted() for alphabetical order.

# sorted() with lambda key
# sorted(silver, key=lambda r: r["salary"], reverse=True) — sorts by salary descending. [:3] takes the top 3. This is the leaderboard.

def build_gold(silver):
    active  = [r for r in silver if r["active"]]
    sals    = [r["salary"] for r in silver]
    depts   = sorted(set(r["dept"] for r in silver))

    dept_summary = {}
    for dept in depts:
        ds = [r["salary"] for r in silver if r["dept"] == dept]
        dept_summary[dept] = {
            "headcount"    : len(ds),
            "avg_salary"   : round(sum(ds) / len(ds), 2),
            "max_salary"   : max(ds),
            "total_payroll": sum(ds),
        }

    leaderboard = sorted(silver, key=lambda r: r["salary"], reverse=True)
    bands       = {b: len([r for r in silver if r["band"] == b])
                   for b in ["Senior", "Mid", "Junior"]}
    return {
        "pipeline"      : CONFIG["pipeline_name"],
        "run_date"      : CONFIG["run_date"],
        "total_emps"    : len(silver),
        "active_emps"   : len(active),
        "avg_salary"    : round(sum(sals) / len(sals), 2),
        "total_payroll" : sum(sals),
        "total_bonus"   : round(sum(r["bonus"] for r in silver), 2),
        "dept_summary"  : dept_summary,
        "band_dist"     : bands,
        "top3_earners"  : [r["name"] for r in leaderboard[:3]],
        "rejected_count": len(rejected_rows),
    }

gold = build_gold(silver)

# Write 3 output files
with open("silver_output.json", "w") as f: json.dump(silver, f, indent=2)
with open("gold_report.json",   "w") as f: json.dump(gold,   f, indent=2)
with open("error_log.json",     "w") as f: json.dump(rejected_rows, f, indent=2)


# Why three separate JSON files?
# silver_output.json = the clean individual records (one per employee). gold_report.json = the summary/aggregated report. error_log.json = rejected rows for investigation. Keeping them separate mirrors real data warehouse architecture (Silver and Gold layers)

# Medallion Architecture (Bronze → Silver → Gold)
# This is the industry-standard pattern used in Apache Spark, Databricks, and modern data warehouses. Bronze = raw data as-is. Silver = cleaned and validated. Gold = aggregated and ready to query. You just implemented it from scratch in plain Python.

# Push day14_project.py + the 3 JSON output files to GitHub. Write a README: "HR ETL Pipeline — Python ETL using Medallion Architecture". This is a real portfolio project.