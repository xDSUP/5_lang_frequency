import re
from collections import Counter

'''
Created on 25 12 2016
@author: xD_HOHOHO
'''


def load_data(filepath):
    with open(filepath, 'r') as file_text:
        text = file_text.read()
        return text


def get_most_frequent_words(text):
    text = re.sub(r'[\d]', ' ', text)
    all_words = re.split(r'\W+', text.lower())
    return Counter(all_words).most_common(10)

if __name__ == '__main__':
    filepath = input('Введите путь до фаила с текстом(пример: text.txt) :  ')
    if filepath:
        try:
            text = load_data(filepath)
            print("Часто встречающиеся слова:")
            for item in get_most_frequent_words(text):
                print(" '{}' встречается {} раз".format(item[0], item[1]))
        except FileNotFoundError:
            print('Фаил не найден')
    else:
        print('Вы не ввели путь до фаила')
