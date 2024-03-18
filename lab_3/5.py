def kol():
    A = int(input('A:' ))
    B = int(input('B:' ))
    C = int(input('C:' ))
    return A,B,C


def m(A, B, C, a, b, c):
    A = a * A
    B = b * B
    C = c * C
    return A,B,C

A, B, C = kol()

a = 10
b = 5
c = 2

A, B, C = m(A, B, C, a, b, c)
print(A, B, C)
