# SQL Joins — Complete Tutorial (From Scratch)

This tutorial builds a small database of **customers** and **orders**, then uses it to demonstrate every major SQL join type. Copy the whole thing into any SQL engine (MySQL, PostgreSQL, SQLite) and run it top to bottom.

---

## 1. Setup — Create the Database and Tables

```sql
-- Create database (skip this line if using SQLite, it doesn't need it)
CREATE DATABASE learn_joins;
USE learn_joins;

-- Table 1: Customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

-- Table 2: Orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,           -- links back to customers.customer_id
    product VARCHAR(50),
    amount DECIMAL(10,2)
);
```

### Insert Sample Data

Notice on purpose:
- **Customer 4 (Diana)** has no orders.
- **Order 105** has a `customer_id` (99) that doesn't exist in `customers`.

This lets us clearly see the difference between join types later.

```sql
INSERT INTO customers (customer_id, customer_name, city) VALUES
(1, 'Alice', 'Bangalore'),
(2, 'Bob', 'Mumbai'),
(3, 'Charlie', 'Delhi'),
(4, 'Diana', 'Chennai');   -- no orders will reference this customer

INSERT INTO orders (order_id, customer_id, product, amount) VALUES
(101, 1, 'Laptop', 55000.00),
(102, 1, 'Mouse', 500.00),
(103, 2, 'Keyboard', 1500.00),
(104, 3, 'Monitor', 12000.00),
(105, 99, 'Webcam', 2000.00); -- customer_id 99 does not exist in customers
```

### Preview the raw tables

```sql
SELECT * FROM customers;
```
| customer_id | customer_name | city      |
|-------------|---------------|-----------|
| 1           | Alice         | Bangalore |
| 2           | Bob           | Mumbai    |
| 3           | Charlie       | Delhi     |
| 4           | Diana         | Chennai   |

```sql
SELECT * FROM orders;
```
| order_id | customer_id | product  | amount   |
|----------|-------------|----------|----------|
| 101      | 1           | Laptop   | 55000.00 |
| 102      | 1           | Mouse    | 500.00   |
| 103      | 2           | Keyboard | 1500.00  |
| 104      | 3           | Monitor  | 12000.00 |
| 105      | 99          | Webcam   | 2000.00  |

---

## 2. INNER JOIN

**Returns only rows that match in both tables.** Diana (no orders) and order 105 (unknown customer) both disappear.

```sql
SELECT c.customer_name, o.product, o.amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;
```

**Result:**
| customer_name | product  | amount   |
|---------------|----------|----------|
| Alice         | Laptop   | 55000.00 |
| Alice         | Mouse    | 500.00   |
| Bob           | Keyboard | 1500.00  |
| Charlie       | Monitor  | 12000.00 |

> Use INNER JOIN when you only care about records that exist on both sides — e.g., "show me customers who actually placed orders."

---

## 3. LEFT JOIN (LEFT OUTER JOIN)

**Returns everything from the left table**, plus matches from the right. Unmatched left rows get `NULL` on the right side. Diana now appears with `NULL` order info.

```sql
SELECT c.customer_name, o.product, o.amount
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;
```

**Result:**
| customer_name | product  | amount   |
|---------------|----------|----------|
| Alice         | Laptop   | 55000.00 |
| Alice         | Mouse    | 500.00   |
| Bob           | Keyboard | 1500.00  |
| Charlie       | Monitor  | 12000.00 |
| Diana         | NULL     | NULL     |

> Use LEFT JOIN to find "all customers, whether or not they ordered anything" — great for finding **inactive customers**:
```sql
SELECT c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;   -- customers with NO orders
```
Result: `Diana`

---

## 4. RIGHT JOIN (RIGHT OUTER JOIN)

**Returns everything from the right table**, plus matches from the left. Unmatched right rows get `NULL` on the left. Order 105 (customer_id 99, which doesn't exist) now appears.

```sql
SELECT c.customer_name, o.product, o.amount
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id;
```

**Result:**
| customer_name | product  | amount   |
|---------------|----------|----------|
| Alice         | Laptop   | 55000.00 |
| Alice         | Mouse    | 500.00   |
| Bob           | Keyboard | 1500.00  |
| Charlie       | Monitor  | 12000.00 |
| NULL          | Webcam   | 2000.00  |

> Note: SQLite doesn't support RIGHT JOIN — you can simulate it by swapping table order and using LEFT JOIN instead.

---

## 5. FULL OUTER JOIN

**Returns everything from both tables**, matched where possible, `NULL` where not. Combines LEFT and RIGHT JOIN results — Diana AND order 105 both appear.

```sql
SELECT c.customer_name, o.product, o.amount
FROM customers c
FULL OUTER JOIN orders o
    ON c.customer_id = o.customer_id;
```

**Result:**
| customer_name | product  | amount   |
|---------------|----------|----------|
| Alice         | Laptop   | 55000.00 |
| Alice         | Mouse    | 500.00   |
| Bob           | Keyboard | 1500.00  |
| Charlie       | Monitor  | 12000.00 |
| Diana         | NULL     | NULL     |
| NULL          | Webcam   | 2000.00  |

> **MySQL doesn't support FULL OUTER JOIN directly.** Simulate it with:
```sql
SELECT c.customer_name, o.product, o.amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT c.customer_name, o.product, o.amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;
```

---

## 6. CROSS JOIN

**Every row of the left table paired with every row of the right table** (Cartesian product) — no `ON` condition. With 4 customers × 5 orders, this produces **20 rows**.

```sql
SELECT c.customer_name, o.product
FROM customers c
CROSS JOIN orders o;
```

**Result (first few rows shown, 20 total):**
| customer_name | product  |
|---------------|----------|
| Alice         | Laptop   |
| Alice         | Mouse    |
| Alice         | Keyboard |
| Alice         | Monitor  |
| Alice         | Webcam   |
| Bob           | Laptop   |
| ...           | ...      |

> Rarely used directly in reports — mostly useful for generating combinations, like pairing every product with every size/color variant.

---

## 7. SELF JOIN

**A table joined with itself** — useful for hierarchical or comparative data (e.g., employees and their managers). Let's add a quick example table:

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT
);

INSERT INTO employees (emp_id, emp_name, manager_id) VALUES
(1, 'Ravi', NULL),      -- Ravi is the top boss, no manager
(2, 'Sneha', 1),        -- Sneha reports to Ravi
(3, 'Amit', 1),         -- Amit reports to Ravi
(4, 'Priya', 2);        -- Priya reports to Sneha

SELECT e.emp_name AS employee, m.emp_name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.emp_id;
```

**Result:**
| employee | manager |
|----------|---------|
| Ravi     | NULL    |
| Sneha    | Ravi    |
| Amit     | Ravi    |
| Priya    | Sneha   |

---

## 8. Quick Reference Cheat Sheet

| Join Type       | Keeps unmatched rows from... | Common use case                          |
|-----------------|-------------------------------|-------------------------------------------|
| INNER JOIN      | Neither                       | Only matching records from both tables    |
| LEFT JOIN       | Left table                    | "All of A, plus matches from B"           |
| RIGHT JOIN      | Right table                   | "All of B, plus matches from A"           |
| FULL OUTER JOIN | Both tables                   | Everything, matched where possible        |
| CROSS JOIN      | N/A (no condition)            | Every possible combination                |
| SELF JOIN       | Depends on join type used      | Comparing rows within the same table      |

### Visual intuition (Venn diagram style)
- `INNER JOIN` = intersection only
- `LEFT JOIN` = left circle entirely + intersection
- `RIGHT JOIN` = right circle entirely + intersection
- `FULL OUTER JOIN` = both circles entirely

---

## 9. Practice Exercises

Try writing these yourself using the tables above:

1. List every customer along with the total amount they've spent (hint: `LEFT JOIN` + `GROUP BY` + `SUM`).
2. Find customers who have never placed an order.
3. Find any orders that reference a customer that doesn't exist (a "data integrity" check).
4. Using the `employees` table, list every employee and how many people report directly to them.

<details>
<summary>Click for solutions</summary>

```sql
-- 1. Total spent per customer
SELECT c.customer_name, COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

-- 2. Customers with no orders
SELECT c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- 3. Orphaned orders (bad customer_id)
SELECT o.*
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- 4. Direct reports count
SELECT m.emp_name AS manager, COUNT(e.emp_id) AS direct_reports
FROM employees m
LEFT JOIN employees e ON e.manager_id = m.emp_id
GROUP BY m.emp_name;
```
</details>

---

## 10. Cleanup (optional)

```sql
DROP TABLE orders;
DROP TABLE customers;
DROP TABLE employees;
DROP DATABASE learn_joins;
```
