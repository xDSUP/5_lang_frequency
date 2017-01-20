import re
import os
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        print('Фаил не найден')
        return None
    with open(filepath, 'r') as file_handler:
        text = file_handler.read()
        return text


def get_most_frequent_words(text):
    treated_text = re.sub(r'[\d]', ' ', text)
    all_words = re.split(r'\W+', treated_text.lower())
    ten_frequent_words = Counter(all_words).most_common(10)
    return ten_frequent_words


def print_frequent_words(frequent_words):
    print("Часто встречающиеся слова:")
    for pair in frequent_words:
        print("Слово '{}' встречается {} раз".format(pair[0], pair[1]))


if __name__ == '__main__':
    filepath = input('Введите путь до фаила с текстом(пример: text.txt) :  ')
    text = load_data(filepath)
    frequent_words = get_most_frequent_words(text)
    print_frequent_words(frequent_words)
