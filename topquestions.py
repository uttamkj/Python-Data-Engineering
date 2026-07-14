# •	Reverse String -----Time Complexity: O(n)
text = 'I love cricket'
def reverse_string(text):
    rev  = ''
    for i in text:
        rev = i+rev
    return rev

# print(reverse_string(text))

# •	Reverse List -----Time Complexity: O(n)
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


# •	Reverse Integer  ----Time Complexity: O(log n)
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

# •	Palindrome  -Time Complexity: O(n)
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

num = 29
def prime(num):

    if num <2:
        return False

    for i in range(2,int(num**0.5)+1):

        if num%i==0:
            return False

    return True

print(prime(num))


# •	Factorial 
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i 
    return fact
# print(factorial(5))


# •	Armstrong Number 
def armstrong_number(num):
    temp = num
    sum = 0
    digits = len(str(num))
    while num > 0:
        last = num % 10
        sum = sum + last**digits
        num = num//10
    return temp == sum

# print(armstrong_number(153))

# •	Anagram 
def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    freq = {}
    freq2 ={}
    for i in str1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    for i in str2:
        if i in freq2:
            freq2[i]+=1
        else:
            freq2[i] = 1

    return freq == freq2

# print(anagram('cccc','cccc'))

# •	Remove Duplicates 
lst = [1,2,1,1,1,2,3,4,5,6,1,2,3,4,5,6,9]
def remove_duplicate(lst):
    seen = set()
    ans = []
    for i in lst:
        if i not in seen:
            ans.append(i)
            seen.add(i)
    return ans

# print(remove_duplicate(lst))


#---------------------------------------------------------------------------------------------------
# •	Flatten Nested List  - Recursion
x=[1,[2,3],[4,[5,6],[7,[8,9]]]]
def flatten(lst):
    result=[]
    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
# print(flatten(x))

# •	Two Sum 
nums=[2,11,15,7]
target=9
def two_sum(nums,target):
    d = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff],i]
        d[num] = i

print(two_sum(nums,target))
# •	Stock Buy Sell  -- Greedy 
prices=[7,1,5,3,6,4]

def max_profit(prices):

    buy=prices[0]
    profit=0

    for price in prices:

        if price<buy:
            buy=price

        elif price-buy>profit:
            profit=price-buy

    return profit

print(max_profit(prices))

# •	Longest Common Prefix 
words=["flower","flow","flight"]

def longest_prefix(words):

    prefix=words[0]

    for word in words[1:]:

        while not word.startswith(prefix):
            prefix=prefix[:-1]

    return prefix

print(longest_prefix(words))
# •	Merge Intervals 
intervals=[[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):

    intervals.sort()

    result=[intervals[0]]

    for current in intervals[1:]:

        last=result[-1]

        if current[0]<=last[1]:
            last[1]=max(last[1],current[1])

        else:
            result.append(current)

    return result

print(merge_intervals(intervals))
# •	Rotate Array 
nums=[1,2,3,4,5,6,7]
k=3

def rotate(nums,k):

    n=len(nums)

    k%=n

    return nums[-k:]+nums[:-k]

print(rotate(nums,k))

# ----------------------------------------------------------------------------------------
# •	Binary Search 
lst = [1,2,3,4,5,6,7,8,9,10]
def binary_search(lst,target):
    st = 0
    end = len(lst)-1
    while st < end:
        mid = (st + end) //2
        if lst[mid] == target :
            return mid
        elif lst[mid] < target:
            st = mid+1
        else : 
            end = mid -1
    return -1
# print(binary_search(lst,9))

# •	Kadane Algorithm  ----Dynamic Programming
nums=[-2,1,-3,4,-1,2,1,-5,4]

def kadane(nums):

    current=nums[0]
    maximum=nums[0]

    for i in nums[1:]:

        current=max(i,current+i)
        maximum=max(maximum,current)

    return maximum

print(kadane(nums))
# •	Sliding Window  -- Maximum Sum Window
nums=[2,1,5,1,3,2]
k=3

def sliding_window(nums,k):

    window=sum(nums[:k])

    maximum=window

    for i in range(k,len(nums)):

        window+=nums[i]-nums[i-k]

        maximum=max(maximum,window)

    return maximum

print(sliding_window(nums,k))


# •	Frequency Count 
def count_frequency(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i]+=1
        else :
            freq[i]=1
    return freq
# print(count_frequency("uttam"))
# print(count_frequency([1,2,3,4,1,1,2,2,2,2,3]))

# •	Top K Frequent 
def top_kFrequent_element(lst,k):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i]+=1
        else :
            freq[i]=1
    for i in freq:
        if freq[i] == k:
            return i
    return -1

# print(top_kFrequent_element([1,2,3,4,1,1,2,2,2,2,3],5))

# •	Missing Number 
def missing_number(lst):
    total = sum(lst)
    n = len(lst)+1
    real = n*(n+1) // 2
    return real-total

# print(missing_number([1,2,3,4,5,7]))

# •	First Non-Repeating Character
text="aabbcdde"
def first_non_repeating(text):
    freq={}
    for ch in text:
        freq[ch]=freq.get(ch,0)+1
    for ch in text:
        if freq[ch]==1:
            return ch
    return None
# print(first_non_repeating(text))


'''
| Pattern             | Problems                                                                        |
| ------------------- | ------------------------------------------------------------------------------- |
| String              | Reverse String, Palindrome, Anagram, Longest Common Prefix, First Non-Repeating |
| Array/List          | Reverse List, Remove Duplicates, Rotate Array, Missing Number                   |
| HashMap/Dictionary  | Two Sum, Frequency Count, Top K Frequent, Anagram                               |
| Math                | Prime, Factorial, Fibonacci, Armstrong, Reverse Integer                         |
| Recursion           | Flatten Nested List                                                             |
| Searching           | Binary Search                                                                   |
| Greedy              | Stock Buy Sell                                                                  |
| Dynamic Programming | Kadane Algorithm                                                                |
| Sliding Window      | Maximum Sum Window                                                              |
| Intervals           | Merge Intervals                                                                 |

'''