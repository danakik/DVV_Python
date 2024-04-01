def count(letter):
    
    with open('2.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        count = content.casefold().count(letter.casefold())
        return count


letter = input('').strip()
count = count(letter)
print(f'літера "{letter}" кількість: {count}')
