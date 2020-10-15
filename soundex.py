import os
import re

from inverted_index import *

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

def removing_the_consecutive_digits(word):
    words = []
    for index,letters in enumerate(word):
        if index == 0:
            if letters[index] == letters[index + 1]:
                words = letters
            else:
                words = letters
        elif index+2 == len(word):



def soundex_vocabulary(inverted_index_map, soundex_index_map):
    for key in inverted_index_map:
        for i, letter in enumerate(key):
            if i == 0:
                soundex_value = letter
            else:
                value = rules_of_soundex(letter)
                soundex_value = soundex_value + str(value)

        removing_the_consecutive_digits(soundex_value)



soundex_vocabulary(inverted_index_map, soundex_index_map)