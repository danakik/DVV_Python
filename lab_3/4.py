import math

def p():
    num = []
    n = int(input('n: '))
    for _ in range(n):
        a = float(input('num:' ))
        num.append(a)
    return num, n


num, n = p()
print(num)
t1 = 0
t2 = 0



for i in range(len(num)):
    if i <  round(len(num) / 2) and num[i] > 0:
        t1 += 1
    elif i >  round(len(num) / 2) and num[i] > 0:
        t2 += 1

print(t1, t2)

k = round(len(num) / 2)
if n / 2 != 0:
    for i in range(k):
        num[i] = math.ceil(num[i])
    for i in range(k, len(num)):
        num[i] = math.floor(num[i])
else:
    for i in range(k):
        num[i] = math.floor(num[i])
    for i in range(k, len(num)):
        num[i] = math.ceil(num[i])  

print(num)