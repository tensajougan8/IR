import os
import re

from inverted_index import *
from itertools import groupby,zip_longest

words = []
outputlist = []
inverted_index_map = dict()
soundex_index_map = dict()

path = r"C:\Users\Valdo\Desktop\test\soundex"
#making inverted index using the function from the imported file
inverted_index(words,inverted_index_map,path)
print(inverted_index_map)

def rules_of_soundex(character):
    if character in ('a','e','o','u','i','h','w','y'):
        return 0
    elif character in ('b','f','p','v'):
        return 1
    elif character in ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'):
        return 2
    elif character in ('d' , 't'):
        return 3
    elif character in ('l'):
        return 4
    elif character in ('m' , 'n'):
        return 5
    elif character in ('r'):
        return 6

def removing_the_consecutive_digits(word):#removes consecutive digits from the given

    res = [i for i, j in zip_longest(word, word[1:])
     if i != j]

    result = list(filter(lambda num: num != '0', res))
    length = len(result)
    if len(result) == 4:
        str1 = ""
        # using join function join the list s by
        # separating words by str1
        return (str1.join(result))
    elif len(result) < 4:
        num = 4 - len(result)
        for x in range(0, num):
            result.append('0')
        str1 = ""
        # using join function join the list s by
        # separating words by str1
        return (str1.join(result))
    elif len(result) > 4:
        result = result[:4]
        str1 = ""
        # using join function join the list s by
        # separating words by str1
        return (str1.join(result))




def soundex_vocabulary(inverted_index_map, soundex_index_map):#gives values to the words
    for key in inverted_index_map:
        for i, letter in enumerate(key):
            if i == 0:
                soundex_value = letter
            else:
                value = rules_of_soundex(letter)
                soundex_value = soundex_value + str(value)

        soundex_word = removing_the_consecutive_digits(soundex_value)

        if soundex_word in soundex_index_map.keys():
            y = []
            x = soundex_index_map[soundex_word]
            y.append(x)
            y.append(key)
            soundex_index_map[soundex_word] = y
        else:
            soundex_index_map[soundex_word] = key


def convert_to_soundex(query):
    word_list = []
    expression = list(query.split())

    for word in expression:
        for i, letter in enumerate(word):
            if i == 0:
                soundex_value = letter
            else:
                value = rules_of_soundex(letter)
                soundex_value = soundex_value + str(value)

        soundex_word = removing_the_consecutive_digits(soundex_value)
        if soundex_word in soundex_index_map:
            if isinstance(soundex_index_map[soundex_word], list):
               of_list = []
               of_list = list(soundex_index_map[soundex_word])
               for i in of_list:
                   word_list.append(i)
            else:
                word_list.append(soundex_index_map[soundex_word])
        else:
            print(word," dosen't exist")
    return word_list

def find_documents(words):
    docs = []
    a = len(words)
    if a == 1:
        str1 = " "
        x = str1.join(words)
        if x in inverted_index_map:
            if isinstance(inverted_index_map[x], list):
                doc = list(inverted_index_map[x])
                for i in doc:
                    docs.append(i)
            else:
                docs.append(inverted_index_map[x])
    else:
        for i in words:
            if i in inverted_index_map:
                if isinstance(inverted_index_map[i],list):
                    doc = list(inverted_index_map[i])
                    for i in doc:
                        docs.append(i)
                else:
                    docs.append(inverted_index_map[i])
    return docs


soundex_vocabulary(inverted_index_map, soundex_index_map)
print(soundex_index_map)
query = input('\nEnter\n')
words = convert_to_soundex(query)
result = find_documents(words)
result = list(dict.fromkeys(result))
print(result)
