# Day 2 Practice — Variables and Data Types # Replace the values below with YOUR actual details 
name = "Your Name" # str 
age = 22 # int 
city = "Bengaluru" # str 
course = "MCA" # str 
target_salary = 500000.00 # float 
is_learning = True # bool 
days_completed = 2 # int 
# Print all details 
print("Name:", name) 
print("Age:", age) 
print("City:", city) 
print("Course:", course) 
print("Target Salary: ₹", target_salary) 
print("Currently learning:", is_learning) 
print("Days completed:", days_completed) 
# Check all types 
print("--- Data Types ---") 
print(type(name)) 
print(type(age)) 
print(type(target_salary)) 
print(type(is_learning))


# Day 3 Task — Numbers, Strings, Casting # Simulating raw CSV data (everything is a string) 
emp_id = "201" 
emp_name = " priya sharma " 
department = "DATA ENGINEERING" 
salary = "82500.75" 
experience = "3" 
is_active = "1" 

# --- CLEAN AND CAST --- 
emp_id = int(emp_id) 
emp_name = emp_name.strip().title() 
# .title() capitalises each word 
department = department.lower() 
salary = float(salary) 
experience = int(experience) 
is_active = bool(int(is_active)) 
# --- CALCULATE bonus (10% of salary) --- 
bonus = round(salary * 0.10, 2) 
# --- PRINT cleaned record --- 
print("===== Cleaned Employee Record =====") 
print(f"ID : {emp_id}") 
print(f"Name : {emp_name}") 
print(f"Department : {department}") 
print(f"Salary : ₹{salary}") 
print(f"Experience : {experience} years") 
print(f"Active : {is_active}") 
print(f"Bonus : ₹{bonus}")

# Day 4 Task — Booleans and Operators # Employee Eligibility Checker for a Promotion # Employee data (try changing these values and re-run) 
emp_name = "Priya Sharma" 
salary = 72000 
experience = 4 
dept = "engineering" 
is_active = True 
has_violation= False 
manager_dept = None  # no manager assigned yet 
# --- ELIGIBILITY RULES --- 
rule1 = salary >= 60000 
rule2 = experience >= 3 
rule3 = dept in ["engineering", "product", "data"] 
rule4 = is_active == True 
rule5 = not has_violation 
rule6 = manager_dept is None # no manager = can be promoted to lead 
# --- FINAL DECISION --- 
eligible = rule1 and rule2 and rule3 and rule4 and rule5 
# --- PRINT REPORT --- 
print(f"===== Promotion Eligibility: {emp_name} =====") 
print(f"Salary >= 60k : {rule1}") 
print(f"Experience >= 3yr : {rule2}") 
print(f"Valid department : {rule3}") 
print(f"Currently active : {rule4}") 
print(f"No violations : {rule5}") 
print(f"No manager yet : {rule6}") 
print(f"---") 
print(f"RESULT: Eligible for promotion = {eligible}")