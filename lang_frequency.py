import re
'''
Created on 25 12 2016
@author: xD_HOHOHO
'''

def load_data(filepath = 'text.txt'):#открывает фаил с текстом, очищает текст от лишних символов и возвращает его программе
    with open(filepath,'r') as file_text:
        return re.sub(r'[`~#1234567890=\+\*\_&\?!\.\$\@,\-;:"\'\n\(\)\[\]\{\}\\/\|]',' ', file_text.read())

def get_most_frequent_words(text): 
    all_words = re.findall(r'\w+',text)
    words_with_the_number_of_meetings = collections.defaultdict(int) #словарь со всеми словами и колличеством в тексте
    for word in all_words:
        words_with_the_number_of_meetings[word.lower()]+= 1 
    return sorted(words_with_the_number_of_meetings.items(), key=lambda x: x[1], reverse=True)[0:10]

if __name__ == '__main__':
    print("Программа найдет самые частые слова в любом тексте.")
    filepath = input('Введите путь до фаила с текстом(пример: text.txt) :  ')        
    text = load_data(filepath)#текст в форме строки без всех знаков препинания
    words_and_counts = get_most_frequent_words(text)#10 слов и количесво их в тексте
    
    print("Часто встречающиеся слова:")
    for item in words_and_counts:
        print(words_and_counts.index(item)+1, " '{}' встречается {} раз".format(item[0], item[1]))
