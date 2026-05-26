
'''
Question 1 : 
You receive raw employee data as strings (like from a CSV). Clean and cast each field, then print a formatted profile card using an f-string.

Given:
emp_id = "205"   name = " ananya reddy "   salary = "93500.0"   experience = "5"   active = "1"

Expected output:
ID: 205 | Name: Ananya Reddy | Salary: ₹93500.0 | Exp: 5 yrs | Active: True
'''

# Raw data from CSV 
emp_id = "205" 
name = " ananya reddy " 
salary = "93500.0" 
experience = "5" 
active = "1" 
# Clean and cast 
emp_id = int(emp_id) 
name = name.strip().title() 
salary = float(salary) 
experience = int(experience) 
active = bool(int(active)) 

print(f"ID: {emp_id} | Name: {name} | Salary: ₹{salary} | Exp: {experience} yrs | Active: {active}")


'''
Question 2 :
Write a program that checks if an employee qualifies for a performance bonus.

Rules: salary must be below ₹80,000 AND experience ≥ 3 years AND department must be "engineering" or "data" AND no active violations.

Print: Each rule result (True/False) and the final ELIGIBLE or NOT ELIGIBLE verdict.


'''
name = "Raj Verma" 
salary = 67000 
experience = 4 
dept = "data" 
violation = False 

r1 = salary < 80000 
r2 = experience >= 3 
r3 = dept in ["engineering", "data"] 
r4 = not violation 

eligible = r1 and r2 and r3 and r4 
print(f"Salary < 80k : {r1}") 
print(f"Experience 3+ : {r2}") 
print(f"Valid dept : {r3}") 
print(f"No violation : {r4}") 
print(f"\nResult: {'ELIGIBLE ✅' if eligible else 'NOT ELIGIBLE ❌'}")


'''
Question 3 :

Given a list of salary records, perform analysis using list operations.

Tasks: Find total, average, max, min salary. Add a new salary. Sort descending. Print the top 3 earners. Store the analysis summary as a tuple.
'''
salaries = [45000, 72000, 88000, 55000, 91000] 
total = sum(salaries)
average = total / len(salaries)
max_salary = max(salaries)
min_salary = min(salaries)
salaries.append(95000)
salaries.sort(reverse=True)
top_3 = salaries[:3]
analysis_summary = (total, average, max_salary, min_salary)

print(f"{analysis_summary}")


'''
Question 4 :
You have two lists of employee IDs from two different source systems. 
Find: IDs in both systems, 
IDs only in system A, 
IDs only in system B, 
and all unique IDs combined.

system_a = [101,102,103,104,105,102,103]   (has duplicates!)
system_b = [103,104,105,106,107]
'''
system_a = [101,102,103,104,105,102,103] 
system_b = [103,104,105,106,107] 
set_a = set(system_a) # {101,102,103,104,105} 
set_b = set(system_b) # {103,104,105,106,107} 
in_both = set_a & set_b 
only_in_a = set_a - set_b 
only_in_b = set_b - set_a 
all_ids = set_a | set_b 
print(f"System A unique IDs : {set_a}") 
print(f"In both systems : {in_both}") 
print(f"Only in System A : {only_in_a}") 
print(f"Only in System B : {only_in_b}") 
print(f"All unique IDs : {all_ids} ({len(all_ids)} total)") 

'''
Question 5 :

Process a list of employee dictionaries (like a JSON API response). For each record: clean the name, cast salary to float, add a "bonus" key (10% of salary), and print a formatted summary. Finally print the total bonus payout.
'''
records = [ {"id":101, "name":" ravi kumar ", "salary":"75000"}, {"id":102, "name":" priya sharma ", "salary":"88000"}, {"id":103, "name":" ankit singh ", "salary":"52000"}, ] 
total_bonus = 0 
print("===== PROCESSED RECORDS =====") 
for emp in records: 
    emp["name"] = emp["name"].strip().title() 
    emp["salary"] = float(emp["salary"]) 
    emp["bonus"] = round(emp["salary"] * 0.10, 2) 
    total_bonus += emp["bonus"] 
    print(f"[{emp['id']}] {emp['name']:15} Salary: ₹{emp['salary']} Bonus: ₹{emp['bonus']}") 
print(f"\nTotal bonus payout : ₹{round(total_bonus,2)}")