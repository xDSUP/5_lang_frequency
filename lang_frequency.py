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
    return words 
def get_ten_frequent_words(words_dict):
    number_occurrences = sorted(words_dict.values())[-10:][::-1]
    frequent_words = [x for x in range(0,10)]
    for word in words_dict:
        for number in range(0,len(number_occurrences)):
            if words_dict[word] == number_occurrences[number] and word not in frequent_words:
                 number_occurrences[number] = 0
                 frequent_words[number] = word
    number_word = sorted(words_dict.values())[-10:][::-1]
    return number_word,frequent_words   

if __name__ == '__main__':
    print("""

Программа найдет самые частые слова в любом тексте.

""")
    while True:
        try:
            filepath = input('Введите путь до фаила с текстом(пример: text.txt) :  ')
            text = load_data(filepath) 
        except EOFError:
            text = load_data()
        except FileNotFoundError:
            print("""
Введите правильный путь
""")
        
        else:
            break
         
    words_dict = get_most_frequent_words(text)
    words_and_numbers = get_ten_frequent_words(words_dict)
    print(print_txt)
    for num in range(0,10):
        print(num, '. ', words_and_numbers[1][num], ' [', words_and_numbers[0][num], ']')
