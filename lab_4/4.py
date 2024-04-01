def count(filename):
    with open(filename, 'r') as file:
        content = file.read()
        num_characters = len(content.replace(" ", "").replace("\n", ""))
        return num_characters


filename = '4.txt'
num_characters = count(filename)
print(f'Кількість символів {num_characters}')
