# •	Reverse String 
text = 'I love cricket'
def reverse_string(text):
    rev  = ''
    for i in text:
        rev = i+rev
    return rev

# print(reverse_string(text))

# •	Reverse List 
lst = [10,20,30,40,50,60,70]
def reverse_list(lst):
    result = []
    for i in range(len(lst)-1,-1,-1):
        result.append(lst[i])
    return(result)
    
# print(reverse_list(lst))

def reverse_in_place(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swap elements using Python's tuple unpacking
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

def reverseList(lst):
    return lst[::-1]
# print(reverseList(lst))


# •	Reverse Integer 
def reverse_intiger(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    ans = 0
    while(num > 0):
        last_digit = num % 10
        ans = (ans*10) + last_digit
        num = num // 10
    return ans*sign
# print(reverse_intiger(-97))

# •	Palindrome 
def check_palindrom(text):
    ans = ''
    for  i in text:
        ans = i+ans
    return ans == text

# print(check_palindrom('madam'))

def palindrome(text):
    left = 0
    right = len(text)-1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


# •	Fibonacci 
def fibonacci_series(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a,b = b,a+b
    return result

# print(fibonacci_series(10))


# •	Prime Number 
def check_prime_number(num):
    if num < 2:
        return False
    for i in range(2,num-1):
        if num% i == 0:
            return False
    return True

# print(check_prime_number(17))
def prime_number_list(st,end):
    ans = []
    for i in range(st,end):
        if check_prime_number(i):
            ans.append(i)
    return ans

# print(prime_number_list(1,20))


# •	Factorial 
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i 
    return fact
# print(factorial(5))


# •	Armstrong Number 

# •	Anagram 
# •	Remove Duplicates 
# •	Flatten Nested List 
# •	Two Sum 
# •	Stock Buy Sell 
# •	Longest Common Prefix 
# •	Merge Intervals 
# •	Rotate Array 
# •	Binary Search 
# •	Kadane Algorithm 
# •	Sliding Window 
# •	Frequency Count 
# •	Top K Frequent 
# •	Missing Number 
# •	First Non-Repeating Character
