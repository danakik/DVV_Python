import math as m
x = int(input())
y = m.acos((x - m.log(x) / (1 + m.cos(3 * x)) + 1))
print(round(y, 3))