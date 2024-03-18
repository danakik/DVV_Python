s = 'це строка або ні но тут має бути двадцять слів, це строка або ні но тут має бути двадцять слів.'

S = ' '.join(map(lambda word: word.capitalize(), s.split()))

print(S)
