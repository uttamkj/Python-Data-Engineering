# Data Engineering — Frequently Asked Interview Questions

Compiled around your syllabus: Python, SQL, Pandas, Apache Spark/PySpark, AWS, Azure/Databricks, plus core Data Engineering concepts.

---

## 1. SQL (asked in almost every DE interview)

1. **What is the difference between `WHERE` and `HAVING`?**
   `WHERE` filters rows before grouping/aggregation; `HAVING` filters groups after `GROUP BY` is applied.

2. **Explain the different types of JOINs.**
   INNER JOIN (matching rows only), LEFT/RIGHT JOIN (all rows from one side + matches), FULL OUTER JOIN (all rows from both, with NULLs where no match), SELF JOIN (table joined with itself), CROSS JOIN (cartesian product).

3. **What's the difference between `DELETE`, `TRUNCATE`, and `DROP`?**
   `DELETE` removes rows (can be filtered, logged, rollback possible), `TRUNCATE` removes all rows fast (minimal logging, resets identity, usually can't rollback), `DROP` removes the entire table structure.

4. **Difference between `UNION` and `UNION ALL`?**
   `UNION` removes duplicates (extra sort/dedup cost); `UNION ALL` keeps all rows including duplicates and is faster.

5. **What is a Primary Key vs a Foreign Key?**
   Primary Key uniquely identifies each row (no NULLs, unique); Foreign Key references a Primary Key in another table to enforce referential integrity.

6. **What are Window Functions? Give examples.**
   Functions that compute a value across a set of rows related to the current row without collapsing them, e.g. `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`, `SUM() OVER (PARTITION BY ...)`.

7. **Difference between `RANK()`, `DENSE_RANK()`, and `ROW_NUMBER()`.**
   `ROW_NUMBER()` gives unique sequential numbers regardless of ties; `RANK()` gives the same rank to ties but skips subsequent ranks; `DENSE_RANK()` gives the same rank to ties without skipping.

8. **What is a CTE (Common Table Expression)? Why use it over a subquery?**
   A `WITH` clause defining a temporary named result set, improving readability and enabling recursion; unlike nested subqueries, it can be referenced multiple times in the main query.

9. **What are indexes, and how do they affect performance?**
   Data structures (commonly B-trees) that speed up read/lookup queries by avoiding full table scans, at the cost of slower writes and extra storage.

10. **Explain normalization and denormalization. When would you denormalize?**
    Normalization organizes data to reduce redundancy (1NF, 2NF, 3NF); denormalization intentionally introduces redundancy to speed up reads — common in data warehouses/OLAP for query performance.

11. **What is the difference between a clustered and non-clustered index?**
    A clustered index determines the physical storage order of data (one per table); a non-clustered index is a separate structure with pointers back to the data (multiple allowed).

12. **How do stored procedures differ from functions?**
    Stored procedures can perform DML operations, don't have to return a value, and can't be used inline in a `SELECT`; functions must return a value and can be used within SQL expressions.

13. **What's the difference between `EXISTS` and `IN`?**
    `EXISTS` checks for the existence of rows in a subquery (stops at first match, generally faster on large datasets); `IN` compares against a list of values and can behave poorly with NULLs.

14. **How would you find duplicate records in a table?**
    Typically `GROUP BY` the relevant columns with `HAVING COUNT(*) > 1`, or use `ROW_NUMBER() OVER (PARTITION BY ...)` and filter where the row number is greater than 1.

15. **What is a SCD (Slowly Changing Dimension) and what are the types?**
    A modeling technique for handling changes in dimension data over time. 
   Type 1 overwrites old data, 
   Type 2 keeps history with new rows and effective dates, 
   Type 3 keeps limited history in extra columns.

---

## 2. Python

1. **What's the difference between a list, tuple, set, and dictionary?**
   List: ordered, mutable, allows duplicates. Tuple: ordered, immutable. Set: unordered, unique elements. Dictionary: key-value pairs, unordered (insertion-ordered since 3.7), mutable.

2. **What are `*args` and `**kwargs`?**
   `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary — useful for flexible function signatures.

3. **What is a lambda function, and when would you use one?**
   An anonymous, single-expression function (`lambda x: x + 1`), typically used for short throwaway logic passed to functions like `map()`, `filter()`, or `sorted(key=...)`.

4. **Explain list comprehension vs a regular loop.**
   List comprehension (`[x*2 for x in range(10)]`) is a concise, often faster way to build lists compared to writing an explicit `for` loop with `.append()`.

5. **What is the difference between `is` and `==`?**
   `==` compares values for equality; `is` compares object identity (whether both references point to the same object in memory).

6. **What are Python generators, and why are they useful in data engineering?**
   Functions using `yield` that produce values lazily one at a time instead of holding a full collection in memory — critical for processing large datasets or streaming data efficiently.

7. **How does exception handling work in Python (`try`/`except`/`finally`)?**
   Code in `try` runs; if an exception occurs, matching `except` blocks handle it; `finally` always runs regardless, commonly used for cleanup like closing file/DB connections.

8. **What is the difference between deep copy and shallow copy?**
   A shallow copy duplicates the outer object but still references nested objects; a deep copy recursively duplicates everything, so nested objects are fully independent.

9. **What are decorators in Python?**
   Functions that wrap another function to extend/modify its behavior without changing its code, commonly used for logging, timing, or access control (`@decorator_name`).

10. **How do you handle large files that don't fit in memory in Python?**
    Read/process in chunks (e.g. `pandas.read_csv(chunksize=...)`), use generators, or use line-by-line file iteration instead of loading the whole file at once.

11. **What's the difference between a module and a package?**
    A module is a single `.py` file; a package is a directory of modules containing an `__init__.py` file.

12. **How would you connect Python to a database and run a query?**
    Using a DB driver/connector (e.g. `psycopg2`, `pyodbc`, `sqlalchemy`), open a connection, create a cursor, execute the SQL, fetch results, then close the connection — often wrapped with context managers (`with`).

---

## 3. Pandas

1. **How do you read a CSV/JSON file into a DataFrame?**
   `pd.read_csv('file.csv')` and `pd.read_json('file.json')` — with parameters like `sep`, `dtype`, `parse_dates` for tuning.

2. **How do you handle missing values in a DataFrame?**
   `df.isnull().sum()` to detect them, then `df.dropna()` to remove or `df.fillna(value)` to impute (mean/median/forward-fill, etc.), depending on the use case.

3. **Difference between `loc[]` and `iloc[]`?**
   `loc[]` selects by label/index name and condition; `iloc[]` selects by integer position.

4. **How do you remove duplicate rows?**
   `df.drop_duplicates(subset=[...], keep='first')`.

5. **What does `groupby()` do, and how is it typically used?**
   Splits the DataFrame into groups based on column values, applies an aggregation (`sum`, `mean`, `count`, etc.), then combines results — the classic "split-apply-combine" pattern.

6. **How do you merge/join two DataFrames?**
   `pd.merge(df1, df2, on='key', how='inner'/'left'/'right'/'outer')`, similar semantics to SQL joins.

7. **What is the difference between `apply()`, `map()`, and `applymap()`?**
   `map()` works element-wise on a Series; `apply()` works on a Series or DataFrame (row/column-wise, can be more complex); `applymap()` applies element-wise across an entire DataFrame.

8. **How do you convert a column's data type?**
   `df['col'] = df['col'].astype('int')` or `pd.to_datetime()`, `pd.to_numeric()` for more controlled conversions.

9. **What's the difference between `pivot()` and `pivot_table()`?**
   `pivot()` reshapes data without aggregation (fails on duplicate index/column pairs); `pivot_table()` reshapes and aggregates duplicate entries (e.g. with `aggfunc='mean'`).

10. **How would you optimize memory usage for a very large DataFrame?**
    Use appropriate dtypes (`category` for low-cardinality strings, smaller int/float types), read in chunks, drop unneeded columns early, and avoid unnecessary copies.

---

## 4. Apache Spark / PySpark

1. **What is Apache Spark, and why is it faster than Hadoop MapReduce?**
   A distributed processing engine that does in-memory computation (vs MapReduce's disk-based read/write between stages), significantly reducing I/O overhead for iterative workloads.

2. **Explain RDD vs DataFrame vs Dataset.**
   RDD: low-level, distributed collection of objects, no schema, no built-in optimization. DataFrame: distributed collection organized into named columns with schema, optimized via Catalyst. Dataset: type-safe version of DataFrame (JVM languages; PySpark mainly uses DataFrames).

3. **What is a transformation vs an action in Spark?**
   Transformations (`filter`, `map`, `select`) are lazy and build a logical execution plan (DAG); actions (`collect`, `count`, `show`, `write`) trigger actual execution.

4. **What is lazy evaluation, and why does Spark use it?**
   Spark doesn't execute transformations immediately — it builds a DAG and only computes when an action is called, allowing it to optimize the full execution plan before running.

5. **Difference between `repartition()` and `coalesce()`.**
   `repartition()` can increase or decrease partitions and triggers a full shuffle; `coalesce()` only decreases partitions and avoids a full shuffle, making it cheaper for reducing partitions.

6. **What are Broadcast Variables and Accumulators?**
   Broadcast variables efficiently share a read-only copy of data across all worker nodes (useful for small lookup tables in joins); accumulators are write-only variables used to aggregate values (like counters) across executors back to the driver.

7. **What is a Spark shuffle, and why is it expensive?**
   A shuffle redistributes data across partitions/nodes (e.g. during `groupBy`, wide joins) — it involves disk I/O, network transfer, and serialization, making it one of the most performance-critical operations to minimize.

8. **What is the difference between `SparkContext` and `SparkSession`?**
   `SparkContext` was the original entry point for RDD-based operations; `SparkSession` (Spark 2.0+) unifies `SparkContext`, `SQLContext`, and `HiveContext` into a single entry point.

9. **What are Window Functions in PySpark, and when would you use them?**
   Similar to SQL window functions — computations over a defined window/partition of rows (e.g. running totals, rankings) using `Window.partitionBy().orderBy()` with functions like `row_number()`, `rank()`, `lag()`, `lead()`.

10. **Explain `union()` vs `unionByName()`.**
    `union()` combines DataFrames by column position (column names/order must align); `unionByName()` combines by matching column names, which is safer when schemas might be ordered differently.

11. **How do you optimize a slow Spark job?**
    Common approaches: reduce shuffles, use broadcast joins for small tables, cache/persist reused DataFrames, tune partition counts, avoid UDFs where built-in functions suffice, and use appropriate file formats (Parquet over CSV).

12. **What is a UDF, and why should they generally be avoided when possible?**
    A User Defined Function lets you apply custom Python logic to DataFrame columns, but UDFs run outside Spark's Catalyst optimizer and involve serialization overhead — built-in Spark SQL functions are usually much faster.

---

## 5. Data Warehousing, ETL & Core DE Concepts

1. **What is the difference between a Data Warehouse and a Data Lake?**
   A Data Warehouse stores structured, processed data optimized for analytics (schema-on-write); a Data Lake stores raw data in any format (structured, semi-structured, unstructured) with schema-on-read flexibility.

2. **Explain ETL vs ELT.**
   ETL (Extract, Transform, Load) transforms data before loading into the target system; ELT (Extract, Load, Transform) loads raw data first and transforms it inside the target system (common with modern cloud warehouses that have strong compute power).

3. **What is a Data Pipeline, and what are its key components?**
   An automated workflow that moves and transforms data from source(s) to destination(s) — typically involving extraction, transformation/validation, loading, orchestration/scheduling, and monitoring.

4. **What is data partitioning, and why does it matter?**
   Splitting data into smaller, manageable chunks (e.g. by date) to improve query performance and enable parallel processing — reduces the amount of data scanned per query.

5. **What is the Medallion Architecture (Bronze/Silver/Gold)?**
   A layered data design pattern: Bronze holds raw/ingested data, Silver holds cleaned and validated data, Gold holds business-level aggregated data ready for analytics/reporting.

6. **What is idempotency in a data pipeline, and why is it important?**
   The property that re-running a pipeline with the same input produces the same result without duplicating or corrupting data — critical for handling retries and failures safely.

7. **How do you handle schema evolution in a pipeline?**
   Techniques include schema versioning, backward/forward-compatible formats (like Avro/Parquet), validation checks before load, and tools like Delta Lake's schema enforcement/evolution features.

8. **What is Change Data Capture (CDC)?**
   A technique to identify and capture changes (inserts/updates/deletes) in a source system so only the delta is propagated downstream, rather than reprocessing the full dataset.

9. **What file formats are commonly used in data engineering, and why prefer Parquet over CSV?**
   Common formats: CSV, JSON, Avro, ORC, Parquet. Parquet is columnar, compressed, and supports predicate pushdown/schema — leading to much faster analytical query performance and smaller storage footprint than row-based CSV.

10. **What is data orchestration, and what tools have you used (e.g. Airflow)?**
    The process of scheduling, sequencing, and monitoring dependent tasks in a pipeline. Airflow (using DAGs) is a common tool; be ready to discuss task dependencies, retries, and scheduling.

11. **How do you ensure data quality in a pipeline?**
    Validation checks (nulls, duplicates, type/range checks), reconciliation counts between source and target, automated tests, alerting on anomalies, and logging/auditing at each pipeline stage.

12. **What is Delta Lake, and what problem does it solve?**
    A storage layer on top of data lakes (built on Parquet) that adds ACID transactions, schema enforcement/evolution, and time travel — solving reliability issues common in plain data lakes.

---

## 6. Cloud Platforms (AWS & Azure)

1. **What is the difference between S3, EC2, and RDS on AWS?**
   S3 is object storage; EC2 is virtual compute (servers); RDS is a managed relational database service.

2. **What is AWS Redshift, and when would you use it?**
   A managed, columnar data warehouse service optimized for large-scale analytical queries (OLAP), commonly used as the "Gold layer" target for reporting.

3. **What is AWS Lambda, and how does it fit into a data pipeline?**
   A serverless compute service that runs code in response to events (e.g. a new file landing in S3), often used for lightweight, event-driven ETL triggers without managing servers.

4. **What is IAM, and why does it matter for data engineering?**
   Identity and Access Management controls who/what can access AWS resources — critical for securing data pipelines, restricting permissions to least-privilege, and auditing access.

5. **What is Azure Data Factory (ADF), and what's its role?**
   A cloud-based orchestration/ETL service for building, scheduling, and monitoring data pipelines that move and transform data across sources — Azure's equivalent to tools like Airflow combined with managed connectors.

6. **What's the difference between Azure Synapse dedicated SQL pools and serverless SQL pools?**
   Dedicated pools provide reserved, provisioned compute for consistent, high-performance workloads (billed regardless of use); serverless pools are pay-per-query, ideal for ad hoc or unpredictable querying.

7. **What is Databricks, and how does it relate to Spark?**
   A unified analytics platform built around Apache Spark, providing managed clusters, collaborative notebooks, and integrated tools (like Delta Lake, Unity Catalog) for big data processing and ML workflows.

8. **What is Unity Catalog in Databricks?**
   A centralized governance layer for managing data access, permissions, lineage, and auditing across Databricks workspaces.

---

## Tips for the Interview Itself

- **Be ready to write SQL and Python/PySpark live** — practice on a whiteboard or plain text editor without autocomplete.
- **Know trade-offs, not just definitions** — interviewers often ask "why would you choose X over Y" (e.g. ELT vs ETL, Parquet vs CSV, `repartition` vs `coalesce`).
- **Have 1–2 pipeline projects ready to walk through end-to-end** — source, ingestion, transformation logic, orchestration, and how you handled failures/scaling.
- **Expect a system design question** — e.g. "design a pipeline to ingest daily sales data from multiple stores into a warehouse." Structure your answer: sources → ingestion → storage/format → transformation → orchestration → monitoring.

---

*Compiled from your Data Engineering syllabus (BrowseJobs) covering Python, SQL, Pandas, PySpark/Spark, AWS, and Azure/Databricks.*
