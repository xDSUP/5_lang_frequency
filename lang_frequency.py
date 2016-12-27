import collections
'''
Created on 25 12 2016

@author: xD_HOHOHO
'''

print_txt = """
Часто встречающиеся слова:
"""

def load_data(filepath = 'text.txt'):
    file_txt = open(filepath,'r')
    text = file_txt.read()
    file_txt.close()
    return text

def get_most_frequent_words(text):
    delimiter_characters = '`~#1234567890=+*_&?!...$@,.-;:"\'\n()[]{}\/ '
    words = collections.defaultdict (int)
    word = ''
    for symvol in text:
        if symvol not in delimiter_characters:
            word += symvol 
            
        else:
            words[word.lower()]+= 1
            word = '' 
    words.__delitem__('')
    lambda_funs = lambda x: x[1]
    frequent_words = sorted(words.items(), key=lambda_funs, reverse=True)[0:10]
    return frequent_words 

if __name__ == '__main__':
    print("""

Программа найдет самые частые слова в любом тексте.

""")
    filepath = input('Введите путь до фаила с текстом(пример: text.txt) :  ')        
    words_and_numbers = get_most_frequent_words(text)
    print(print_txt)
    for num in range(0,10):
        print(num+1, '. ', words_and_numbers[num][0], ' [', words_and_numbers[num][1], ']')
