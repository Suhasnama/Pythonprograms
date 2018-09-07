import math

data = str(input("Enter alphanumeric string\n"))

n = data[::-1]
print(n)
count = 0
l = []
x = 0
value = 0
try:
    for i in n:
        if i.isdigit():
            value = value + int(i) * int(math.pow(10 , count))
            count = count + 1
            #print("This is from digit ",value)
        else:
            #print("This is from non-digit ",value)
            l.append(value)
            count=0
            value = 0
finally:
    #print("This is from finally ",value)
    l.append(value)
    

# for i in l:
#     x = x + i
import functools

x = functools.reduce(lambda x , y : x + y , l)
print(x)