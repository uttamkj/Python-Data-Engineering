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

