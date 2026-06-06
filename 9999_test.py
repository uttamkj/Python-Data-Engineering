def numbers():
    for i in range(5):
        yield i

# print(numbers())

def passwordChecker():
    attempt = 0
    max_attempt = 3
    password = 'Nokia@123'
    while attempt < max_attempt:
        userPassword = input("Enter your passord : ").strip()
        if userPassword == '':
            print("enter valid input!!")
            break
        if userPassword == password : 
            print("you have been loged in successfully")
            break
        else :
            if attempt < max_attempt:
                print(f"Try again you have {max_attempt - attempt-1} attempts left!!")
                attempt+=1
            else :
                print("You are done with attempts contact to admin")

# passwordChecker()
def isPrime(num):
    if num <= 1 :
        return False
    for i in range(2,num):
        if num % i  == 0 :
            return False
    return True

# num = int(input("Enter your number: "))
# print(isPrime(num))

def isPrimeOptimized(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

import math

def isPrimeOptimized3(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

import random

def generatePassowrd(length):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    lowercase = uppercase.lower()
    numbers = '0123456789'
    spacelCharacters = '!@#$%^&*'

    password = ''
    password = password + random.choice(uppercase)
    password = password + random.choice(lowercase)
    password = password + random.choice(numbers)
    password = password + random.choice(spacelCharacters)

    allcharcters = uppercase+lowercase+spacelCharacters+numbers

    # password+=random.choice(allcharcters)
    # password+=random.choice(allcharcters)
    # password+=random.choice(allcharcters)
    # password+=random.choice(allcharcters)
    reqLength = length - len(password)

    for i in range(reqLength):
        password = password + random.choice(allcharcters)
    return password

# print(generatePassowrd())
print(generatePassowrd(10))
print(len(generatePassowrd(10)))


# print(random.choice('123456789abcd'))

'''
List comperhansion : its a new way to create a new list based on a expression 

'''
x = [1,2,3,4,5,6]

square = []
for i in x:
    square.append(i*i)

# OAC output action condition
square2 = [i*i for i in x]
square3 = [i*i for i in x if i%2 ==0]


print(square2)
print(square3)

print("**************************************")
x = [[1,2,3],[4,5,6],[7,8,9]]

for i in x:
    for j in i:
        print(i)