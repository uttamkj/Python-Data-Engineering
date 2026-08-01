-- find the employee name and thier manager name
select e.emp_name as emp_name ,m.emp_name as manager_name
from employees e
LEFT JOIN employees m
on e.emp_id = m.manager_id
where m.emp_name is not null;


-- Find all employees who report to Rahul Kumar.
select e.emp_name as emp_name ,m.emp_name as manager_name
from employees e
LEFT JOIN employees m
on e.emp_id = m.manager_id
where m.emp_name = 'Neha Gupta';

-- count the employee under each manager
SELECT
m.emp_name,
COUNT(e.emp_id) AS total_employees
FROM employees e
JOIN employees m
ON e.manager_id=m.emp_id
GROUP BY m.emp_name;

-- Find Manager Having Maximum Employees
SELECT
m.emp_name,
COUNT(*) AS total
FROM employees e
JOIN employees m
ON e.manager_id=m.emp_id
GROUP BY m.emp_name
ORDER BY total DESC
LIMIT 1;

-- Show Employees with Their Manager Salary
SELECT
e.emp_name,
e.salary AS employee_salary,
m.emp_name AS manager_name,
m.salary AS manager_salary
FROM employees e
LEFT JOIN employees m
ON e.manager_id=m.emp_id;

-- Employees Earning More Than Their Managers
SELECT
e.emp_name,
e.salary,
m.emp_name as manager_name,
m.salary as manager_salary
FROM employees e
JOIN employees m
ON e.manager_id=m.emp_id
WHERE e.salary>m.salary;

