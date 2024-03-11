s = {1, 2, 3, 4, 5}
print(s)

s.add(6)
print(s)

s.remove(3)
print(s)

x = 3
if x in s:
    print(f'{x} є в множині')
else:
    print(f'{x} відсутній в множині')
