x = "I am data enginner with three year of eperience in data engineering and data analysis. I have worked on various projects involving data pipelines, ETL processes, and data visualization. My expertise includes working with big data technologies such as Hadoop, Spark, and Kafka, as well as programming languages like Python and SQL. I am passionate about leveraging data to drive business insights and make informed decisions."
x = x.lower()
s = x.split()

res = {}

for i in s:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

# print(res)

res2 = {}

for ch in x.replace(" ", ""):
    if ch in res2:
        res2[ch] += 1
    else:
        res2[ch] = 1

# print(res2)


text = "Data enginner"
v=0
c=0
for i in text.lower():
    if i in "aeiou":
        v+=1
    elif i.isalpha():
        c+=1

print(f"Vowels: {v}, Consonants: {c}")
#  isAlpha() method returns True if all the characters are alphabet letters (a-z). If not, it returns False.
print("Uttam Kumar".isalpha())  
print("UttamKumar".isalpha())  

word =s[0]
for i in s:
    if len(i)>len(word):
        word=i
print(f"Longest word: {word}, Length: {len(word)}")

s = [1,2,3,4,1,2,3,4,5,6,]
x = set(s)
print(x)

text = "uttam"
print(sorted(text))


x = [1,2,3,4,
     ['apple','banana','mango',
      ['tomato','beans',
       ['pencil','pen','krish'],
       'coriander'],
      'watermelon']]

result = []

def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            result.append(i)

flatten(x)
print(result)