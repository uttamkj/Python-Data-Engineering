x = [80,60,20,10,50,30,90,40]

def bubbleSort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

print(bubbleSort(x))

arr = [10,20,30,40,50,60,70,80]
target = 80
def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch(arr, target))

def largest_element(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

def get_second_largest(arr):
    max_num = float('-inf')
    second_max = float('-inf')
    for num in arr:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num

    return max_num, second_max

def first_nonrepeating_number(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    for num in arr:
        if count[num] == 1:
            return num
    return None

def two_sum(arr, target):
    seen = {}
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

nums = [1, 2, 11, 15, 10, 7, 20]
target = 9

def get_two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return (index, seen[complement])

        seen[num] = index

print(get_two_sum(nums, target))


nums = [1, 2, 3, 2, 4, 5, 1]

def find_duplicates(nums):
    seen = set()
    dups = set()

    for num in nums:
        if num in seen:
            dups.add(num)
        else:
            seen.add(num)

    print(seen, dups)

find_duplicates(nums)


prices = [7, 1, 5, 3, 6, 4]

def get_max(prices):
    max_profit = 0
    min_price = prices[0]

    for price in prices:

        if price < min_price:
            min_price = price

        profit = price - min_price
        max_profit = max(max_profit, profit)

        print(min_price, price, profit, max_profit)

    return max_profit

print(get_max(prices))