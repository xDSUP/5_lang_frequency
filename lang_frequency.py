import collections
import re
'''
Created on 25 12 2016
@author: xD_HOHOHO
'''


def load_data(filepath):  # Загружает и очищает текст от лишних символов
    with open(filepath, 'r') as file_text:
        text = file_text.read()
        text = re.sub(r'[`~#0123456789=\+\*\_&\?!\.\$\@,]', ' ', text)
        text = re.sub(r'[\-;:"\'\n()\[\]\{\}\\/\|]', ' ', text)
        return text


def get_most_frequent_words(text):  # вернет словa и их количесво в тексте
    all_words = re.findall(r'\w+', text)  # список всех слов из текста
    words_and_meetings = collections.defaultdict(int)
    for word in all_words:
        words_and_meetings[word.lower()] += 1
    return sorted(words_and_meetings.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    print("Программа найдет самые частые слова в любом тексте.")
    filepath = input('Введите путь до фаила с текстом(пример: text.txt) :  ')
    text = load_data(filepath)  # текст в форме строки
    words_and_counts = get_most_frequent_words(text)[0:10]
    print("Часто встречающиеся слова:")
    for item in words_and_counts:
        print(" '{}' встречается {} раз".format(item[0], item[1]))
