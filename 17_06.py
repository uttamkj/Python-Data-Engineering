# listmethods 
# append
# extend
# insert 
# remove 
# pop 
# sorted
# sort 
# index 
# count
# a = "I am uttam data engineer in 2026-2027 trying to be a good data engineer, i am  in google learing from multiple source"
# print(a.split(" "))
# print(a.strip())

text = 'I am a data engineer and I deal with data everyday'
frequency = {

}
for word in text.lower().split(" "):
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] = 1

print(frequency)

lst = [5,4,0,6,3,2,7,8,1,9]

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            
    return lst

print(bubbleSort(lst))

text = 'Madam'

def palindromeCheck(text):
    result = ''
    text = text.lower()
    for i in text:
        result = i+result

    return result == text

print(palindromeCheck('Rottor'))

def fibonacciSeries(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacciSeries(10)

