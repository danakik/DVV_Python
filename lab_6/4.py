import matplotlib.pyplot as plt
import string
from collections import Counter

def count_vowels_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = ''.join(filter(lambda x: x.lower() in 'aeiouyаоуеиі', text))
    text = text.lower()
    vowel_count = Counter(text)
    sorted_vowels = sorted(vowel_count.items())

    vowels, frequencies = zip(*sorted_vowels)

    plt.bar(vowels, frequencies)
    plt.title('Гістограма частоти появи голосних літер')
    plt.xlabel('Голосна літера')
    plt.ylabel('Частота')
    plt.show()

file_path = 'lab_6/text.txt'
count_vowels_from_file(file_path)
