#sum of array
arr = [1,2,3,4,5,6,7,8]

def sumOfArray(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum
# print(sumOfArray(arr))


def indexOfAElement(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# print(indexOfAElement(arr,90))

def binarySearch(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return -1

transactions = [101,102,103,104,105,106,104]

def findDuplicate(lst):
    seen = set()
    dup = set()
    for i in lst:
        if i in seen:
            dup.add(i)
        else:
            seen.add(i)
        
    return dup

# print(findDuplicate(transactions))

def first_Occering_duplicate(lst):
    freq ={}
    for i in lst:
        if i in freq:
           freq[i]+=1
        else :
            freq[i] = 1
    # print(freq)
    for key,value in freq.items():
        if freq[key] > 1:
            return key
        
    return -1

# print(first_Occering_duplicate(transactions))

arr = [20,1,3,5,6,7,89,9,0,-21,-4,50,65,176,114,160]
def highestElemt(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

def smallestElement(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

def secondHighestElement(arr):
    if len(arr) < 2:
        return None
    
    max = float('-inf')
    secondHighestElement = float('-inf')
    for i in arr :
        if i > max:
            secondHighestElement = max
            max = i
        elif i >secondHighestElement and i != max:
            secondHighestElement = i
    
    return secondHighestElement

def secondminElement(arr):
    min_val = float('inf')
    sec_min = float('inf')
    for i in arr:
        if i < min_val:
            sec_min = min_val
            min_val = i
        elif i < sec_min and i != min_val:
            sec_min = i
    return sec_min

# print(highestElemt(arr))
# print(smallestElement(arr))
print(secondHighestElement(arr))