x = [1,[2,3],[4,[5,6],[7,[8,9]]]]



y = str(x).replace('[','').replace(']','')
z = '['+ y + ']'
a = eval(z)

def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


x = [1, [2, 3], [4, [5, 6], [7, [8, 9]]]]

print(flatten(x))

name = "Uttam"

rev_name = name[::-1]
print(rev_name)

revName = ""
for i in name:
    revName = i+revName
print(revName)

reverse = ""
for i in range(len(name)-1,-1,-1):
    reverse = reverse+name[i]

print(reverse)

def fibonaciSeries(num):
    list1 = []
    num1 = 0
    num2 = 1
    for i in range(num):
        list1.append(num1)
        num1,num2 = num2,num1+num2
    return list1

# num = int(input("Enter num : "))
# print(fibonaciSeries(num)) 

def flattend(x):
    a = str(x).replace('[','').replace(']','')
    b = '[' + a + ']'
    c = eval(b)
    return(b)

x = [1,2,3,['a','b','c','d'],'e','f','g','h','i',4,5,[6,7,[8,9]],10]

print(flatten(x))

nested = [[1,2,3], [4,5,6], [7,8,9]]
flat = [j for i in nested for j in i]
print(flat)

