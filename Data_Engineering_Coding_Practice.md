# Data Engineering — Coding & Live Assessment Practice

Real problems you'll be asked to solve live (whiteboard, shared editor, or take-home). Each has sample data, the task, and a working solution — try solving it yourself first, then check.

---

## 1. SQL — Query Writing

**Sample schema used throughout this section:**

```sql
CREATE TABLE employees (
    emp_id      INT PRIMARY KEY,
    name        VARCHAR(50),
    dept_id     INT,
    manager_id  INT,
    salary      DECIMAL(10,2),
    hire_date   DATE
);

CREATE TABLE departments (
    dept_id     INT PRIMARY KEY,
    dept_name   VARCHAR(50)
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT,
    order_date  DATE,
    amount      DECIMAL(10,2)
);
```

### Problem 1 — Second highest salary
Find the second highest salary without using `LIMIT`/`OFFSET` (so it works across DB engines).

```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

### Problem 2 — Top N per group
Find the top 2 highest-paid employees in each department.

```sql
SELECT emp_id, name, dept_id, salary
FROM (
    SELECT emp_id, name, dept_id, salary,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk <= 2;
```

### Problem 3 — Find duplicate rows
Find customers who placed more than one order on the same day.

```sql
SELECT customer_id, order_date, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id, order_date
HAVING COUNT(*) > 1;
```

### Problem 4 — Running total
Calculate a running total of order amounts per customer, ordered by date.

```sql
SELECT customer_id, order_date, amount,
       SUM(amount) OVER (
           PARTITION BY customer_id ORDER BY order_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM orders;
```

### Problem 5 — Orphaned foreign keys
Find employees whose department doesn't exist in the `departments` table.

```sql
SELECT e.emp_id, e.name, e.dept_id
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
```

### Problem 6 — Month-over-month growth
Calculate month-over-month total order amount and % growth.

```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS total_amount
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT month, total_amount,
       LAG(total_amount) OVER (ORDER BY month) AS prev_month,
       ROUND(
         (total_amount - LAG(total_amount) OVER (ORDER BY month))
         / LAG(total_amount) OVER (ORDER BY month) * 100, 2
       ) AS pct_growth
FROM monthly
ORDER BY month;
```

### Problem 7 — Employees who earn more than their manager
```sql
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
```

### Problem 8 — Pivot rows to columns (without a native PIVOT keyword)
```sql
SELECT
    SUM(CASE WHEN d.dept_name = 'Sales' THEN e.salary ELSE 0 END) AS sales_total,
    SUM(CASE WHEN d.dept_name = 'Engineering' THEN e.salary ELSE 0 END) AS eng_total
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

### Problem 9 — Gaps and islands (find missing dates)
Find dates in January 2025 with no orders (classic "gap detection" pattern).

```sql
WITH RECURSIVE calendar AS (
    SELECT DATE '2025-01-01' AS dt
    UNION ALL
    SELECT dt + INTERVAL '1 day' FROM calendar WHERE dt < DATE '2025-01-31'
)
SELECT c.dt
FROM calendar c
LEFT JOIN orders o ON c.dt = o.order_date
WHERE o.order_date IS NULL;
```

### Problem 10 — Deduplicate, keeping the latest record
Keep only the most recent order per customer (common CDC-style dedup task).

```sql
DELETE FROM orders
WHERE order_id NOT IN (
    SELECT order_id FROM (
        SELECT order_id,
               ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
        FROM orders
    ) t
    WHERE rn = 1
);
```

---

## 2. Python — Coding Problems

### Problem 1 — Word frequency counter
```python
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

# Cleaner with collections
from collections import Counter
def word_frequency_v2(text):
    return Counter(text.lower().split())
```

### Problem 2 — Flatten a nested list
```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

flatten([1, [2, 3, [4, 5]], 6])  # [1, 2, 3, 4, 5, 6]
```

### Problem 3 — Detect duplicates in a list
```python
def find_duplicates(lst):
    seen, dupes = set(), set()
    for x in lst:
        if x in seen:
            dupes.add(x)
        seen.add(x)
    return list(dupes)
```

### Problem 4 — Group a list of dicts by a key (mimicking `GROUP BY`)
```python
from collections import defaultdict

def group_by_key(records, key):
    grouped = defaultdict(list)
    for r in records:
        grouped[r[key]].append(r)
    return dict(grouped)

data = [{"dept": "Sales", "salary": 50000}, {"dept": "Eng", "salary": 80000},
        {"dept": "Sales", "salary": 55000}]
group_by_key(data, "dept")
```

### Problem 5 — Read a large file line by line without loading it all into memory
```python
def process_large_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

# Usage: for row in process_large_file("huge.csv"): ...
```

### Problem 6 — Merge two dictionaries, summing values on key conflicts
```python
def merge_sum(d1, d2):
    result = dict(d1)
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result
```

### Problem 7 — Implement a simple retry decorator (common in pipeline code)
```python
import time
import functools

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data():
    # e.g. call an unreliable API
    pass
```

### Problem 8 — Parse and validate JSON records, skipping malformed ones
```python
import json

def parse_records(raw_lines):
    valid, invalid = [], []
    for line in raw_lines:
        try:
            record = json.loads(line)
            valid.append(record)
        except json.JSONDecodeError:
            invalid.append(line)
    return valid, invalid
```

### Problem 9 — Two Sum (classic, still asked as a warm-up)
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

### Problem 10 — Chunk a list into batches (common for bulk inserts / batch API calls)
```python
def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

list(chunk_list(list(range(10)), 3))  # [[0,1,2],[3,4,5],[6,7,8],[9]]
```

---

## 3. Pandas — Coding Tasks

**Sample data used below:**

```python
import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer": ["A", "B", "A", "C", "B", "A"],
    "amount": [100, 200, None, 150, 300, 50],
    "order_date": pd.to_datetime(
        ["2025-01-01", "2025-01-02", "2025-01-03",
         "2025-01-03", "2025-01-05", "2025-01-06"]
    )
})
```

### Task 1 — Fill missing amounts with the customer's average
```python
df["amount"] = df.groupby("customer")["amount"].transform(
    lambda x: x.fillna(x.mean())
)
```

### Task 2 — Total and average spend per customer
```python
summary = df.groupby("customer").agg(
    total_spend=("amount", "sum"),
    avg_spend=("amount", "mean"),
    order_count=("order_id", "count")
).reset_index()
```

### Task 3 — Find the top spender
```python
top_customer = summary.loc[summary["total_spend"].idxmax(), "customer"]
```

### Task 4 — Create a running total per customer (mirrors the SQL problem above)
```python
df = df.sort_values(["customer", "order_date"])
df["running_total"] = df.groupby("customer")["amount"].cumsum()
```

### Task 5 — Pivot: orders per customer per day
```python
pivot = df.pivot_table(
    index="customer", columns="order_date",
    values="amount", aggfunc="sum", fill_value=0
)
```

### Task 6 — Detect and flag outliers (values > 2 std devs from mean)
```python
mean, std = df["amount"].mean(), df["amount"].std()
df["is_outlier"] = (df["amount"] - mean).abs() > 2 * std
```

### Task 7 — Merge two DataFrames and identify unmatched rows (anti-join)
```python
customers = pd.DataFrame({"customer": ["A", "B", "D"], "region": ["West", "East", "North"]})

merged = df.merge(customers, on="customer", how="left", indicator=True)
unmatched = merged[merged["_merge"] == "left_only"]
```

---

## 4. PySpark — Coding Tasks

**Sample setup:**

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("practice").getOrCreate()

data = [(1, "A", 100, "2025-01-01"), (2, "B", 200, "2025-01-02"),
        (3, "A", None, "2025-01-03"), (4, "C", 150, "2025-01-03"),
        (5, "B", 300, "2025-01-05"), (6, "A", 50, "2025-01-06")]

df = spark.createDataFrame(data, ["order_id", "customer", "amount", "order_date"])
df = df.withColumn("order_date", F.to_date("order_date"))
```

### Task 1 — Fill nulls with the customer's average amount
```python
avg_by_customer = df.groupBy("customer").agg(F.avg("amount").alias("avg_amt"))
df = df.join(avg_by_customer, on="customer", how="left")
df = df.withColumn("amount", F.coalesce("amount", "avg_amt")).drop("avg_amt")
```

### Task 2 — Running total per customer using Window functions
```python
window_spec = Window.partitionBy("customer").orderBy("order_date")
df = df.withColumn("running_total", F.sum("amount").over(window_spec))
```

### Task 3 — Rank customers by total spend
```python
totals = df.groupBy("customer").agg(F.sum("amount").alias("total_amount"))
rank_window = Window.orderBy(F.desc("total_amount"))
totals = totals.withColumn("rank", F.dense_rank().over(rank_window))
```

### Task 4 — Deduplicate, keeping the latest record per customer
```python
dedup_window = Window.partitionBy("customer").orderBy(F.desc("order_date"))
df_latest = (
    df.withColumn("rn", F.row_number().over(dedup_window))
      .filter(F.col("rn") == 1)
      .drop("rn")
)
```

### Task 5 — Broadcast join a small lookup table (performance-focused question)
```python
region_lookup = spark.createDataFrame(
    [("A", "West"), ("B", "East"), ("C", "North")], ["customer", "region"]
)

df_joined = df.join(F.broadcast(region_lookup), on="customer", how="left")
```

### Task 6 — Write partitioned Parquet output (common take-home task)
```python
df.write.mode("overwrite").partitionBy("customer").parquet("/output/orders")
```

### Task 7 — Word count (the "Hello World" of distributed processing)
```python
text_rdd = spark.sparkContext.parallelize(["hello world", "hello spark", "world of data"])
word_counts = (
    text_rdd.flatMap(lambda line: line.split(" "))
            .map(lambda word: (word, 1))
            .reduceByKey(lambda a, b: a + b)
)
word_counts.collect()
```

---

## 5. Take-Home / System-Design-Style Coding Tasks

These show up as full assessments (1–3 hour take-homes) rather than single functions. Typical prompts:

1. **Build a small ETL script**: Read a CSV of raw transactions, clean it (nulls, duplicates, type casting), aggregate daily totals per customer, and write the result to Parquet or a database table. *(Tests: Pandas/PySpark, file I/O, error handling.)*

2. **Design and implement an incremental load**: Given a source table with a `last_updated` timestamp, write a script that only pulls records changed since the last run and merges (upserts) them into a target table. *(Tests: CDC thinking, SQL MERGE/upsert logic, idempotency.)*

3. **API-to-warehouse pipeline**: Pull paginated data from a REST API (often mocked), handle rate limits/retries, and load it into a database or file store. *(Tests: Python requests handling, retry logic, pagination loops.)*

4. **Data quality checker**: Given a dataset, write a script that flags rows with nulls in required fields, duplicate primary keys, or values outside expected ranges, and outputs a summary report. *(Tests: validation logic, clear code structure, summarization.)*

5. **Debug a broken pipeline**: You're given a script with a bug (e.g. wrong join type causing row explosion, or a Spark job that never finishes due to a skewed key) and asked to find and fix it. *(Tests: debugging under pressure, understanding of joins/shuffles.)*

**How to approach any take-home:**
- Clarify assumptions in comments/README (e.g. "assuming duplicate order_ids should keep the latest record").
- Write it as if it's going into production: small functions, error handling, logging — not a single messy script.
- Include a few test cases or sample outputs, even minimal ones.
- If time-boxed live, narrate your thinking out loud — interviewers weigh your reasoning process as much as the final answer.

---

## 6. Quick Self-Test Checklist

Before an interview, make sure you can do each of these **without looking anything up**:

- [ ] Write a window function query for running total and rank
- [ ] Write a self-join and an anti-join (`LEFT JOIN ... WHERE NULL`)
- [ ] Deduplicate rows in SQL, Pandas, and PySpark, keeping the latest record
- [ ] Write a Python generator for reading a large file
- [ ] Write a retry-with-backoff decorator
- [ ] Fill nulls with a group-wise average in Pandas and PySpark
- [ ] Explain and fix a skewed/slow Spark job in words, even without running it
- [ ] Write a MERGE/upsert statement (SQL or Delta Lake syntax)

---

*Pair this with `Data_Engineering_Interview_FAQs.md` — that file covers the "explain X" questions, this one covers the "now build it" questions.*
