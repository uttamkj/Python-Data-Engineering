
try:
  y = 10/0
  x = int('abc')

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