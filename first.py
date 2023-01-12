import math

arr = []
s = 0
n = 0
while not(num == 0):
    num = int(input())
    arr.append(num)
    s += num
    n += 1

s = s / n
top = 0

for  x in arr:
    top += (x - s) ** 2
    
print(math.sqrt(top / (n - 1))