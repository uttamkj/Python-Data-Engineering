# with open("high.txt", "w") as f :
#     f.write("0")


# def readFile(filepath):
#     with open(filepath,"r") as f:
#         text = f.readline()
#         return text
    

# def game() :
#     # read the highst value 
#     # print(readFile("high.txt"))
#     high_score = int(readFile("high.txt"))
#     # play game 
#     x = int(input("Enter your choice : "))

    
#     # check then if update 
#     if x > high_score:
#         with open("high.txt", "w") as f:
#             f.write(str(x))
#         print(f"New High Score {x} is updated")
#     else:
#         print(f"High Score remains: {high_score}")

# game()

'''
with open("raw_hr_data.csv", "r") as f:
    data = f.read()
    print(data)

id,name,salary,dept,experience,active
101,  ravi kumar  ,75000,engineering,4,1
102,  priya sharma  ,88000,data,6,1
103,  ankit singh  ,N/A,sales,2,1       
104,,91000,engineering,7,1              
105,  sneha rao  ,67000,unknown,3,1   
106,  raj verma  ,62000,data,3,1
107,  meera iyer  ,54000,hr,1,1
108,  karan mehta  ,83000,finance,5,0 '''


'''
with open("raw_hr_data.csv", "r") as f:
    data = f.readline()
    print(data)
id,name,salary,dept,experience,active
'''

'''
with open("raw_hr_data.csv", "r") as f:
    data = f.readlines()
    print(data)

['id,name,salary,dept,experience,active\n', 
 '101,  ravi kumar  ,75000,engineering,4,1\n', 
 '102,  priya sharma  ,88000,data,6,1\n', 
 '103,  ankit singh  ,N/A,sales,2,1       \n', 
 '104,,91000,engineering,7,1              \n', 
 '105,  sneha rao  ,67000,unknown,3,1   \n', 
 '106,  raj verma  ,62000,data,3,1\n', 
 '107,  meera iyer  ,54000,hr,1,1\n', 
 '108,  karan mehta  ,83000,finance,5,0\n']
'''

# def read_csv(filepath):
#     with open(filepath, "r") as f:
#         data = f.readlines()
#         header = data[0].strip().split(",")
#         records = []
#         for line in data[1:]:
#             record = line.strip().split(",")
#             records.append(record)
#         return header, records
    
# header, records = read_csv("raw_hr_data.csv")
# print(header)
# print("-------------")
# print(records)

'''
def read_csv(filepath):
    with open(filepath, "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print(lines)

    headers = [h.strip() for h in lines[0].split(",")]
    print(headers)
    rows = []
    for i, line in enumerate(lines[1:], 2):   # start at line 2
            parts = line.split(",")
            if len(parts) == len(headers):
                row = dict(zip(headers, [p.strip() for p in parts]))
                row["_line"] = i        # track source line for error log
                rows.append(row)
    return rows

t = read_csv("raw_hr_data.csv")

print(t)'''

lines = []
headers = []
with open("raw_hr_data.csv", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

headers = [h.strip() for h in lines[0].split(",")]

# print(lines)
# print(headers)

rows = []
for i, line in enumerate(lines[1:], 2):   # start at line 2
    parts = line.split(",")
    if len(parts) == len(headers):
        row = dict(zip(headers, [p.strip() for p in parts]))
        row["_line"] = i        # track source line for error log
        rows.append(row)

# print(rows)