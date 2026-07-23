
try:
  print("Line 3")
  x = int('abc')
  y = 10/0
  print("Line 6")
except(ZeroDivisionError,ValueError) as e:
  print('Error: ', e)

try:
  file = open('/content/data.csv','r')
  content = file.read()
  print(content)
except FileNotFoundError:
  print('file not found')
else:
  print('file read successfully')
finally:
  print('finally block')


with open('/content/t3.txt','wra') as file:
  file.write('wassup bro')