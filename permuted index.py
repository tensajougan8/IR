import os
import re
import fnmatch
from functools import reduce
from inverted_index import *
import operator

words = []
outputlist = []
inverted_index_map = dict()
permuted_index_map = dict()

path = r"C:\Users\Valdo\Desktop\test\permuted"
#making inverted index using the function from the imported file
inverted_index(words,inverted_index_map,path)
print(inverted_index_map)

#makes the permuted index
def permuted_vocabulary(inverted_index_map, permuted_index_map):
    for key in inverted_index_map:
        word = key + '$'
        # print(word)
        j = len(word)
        count = 0
        for i in word:
            first_slice = (word[:count])
            second_slice = (word[count:])
            join_slice = second_slice + first_slice
            count += 1
            permuted_index_map[join_slice] = key

#appyling the algorithm on the query
def rotate_query(query):
    permuted_query_list = []
    res = len(re.findall(r'\w+', query))
    expression = list(query.split())
    for word in expression:
        star_count = word.count('*')
        if star_count == 0:
            new_word = word + '$'
            permuted_query_list.append(new_word)
        elif star_count == 1:#three conditions i.e *X , X* , X*Y
            if word.endswith('*'):#X* condition
                new_word = '$' + word
                print(new_word)
            elif word[:1] == '*':#*X condition
                new_word = word[1:] + '$' + word[:1]
                print(new_word)
            else:#x*Y condition
                count = 0
                for letter in range(len(word)):
                    if word[letter] == '*':
                        first_slice = (word[:letter+1])
                        second_slice = (word[letter+1:])
                        new_word = second_slice + '$' + first_slice
                        permuted_query_list.append(new_word)
        elif star_count >= 2:
            #pattern is *X*
            pattern_first = '^\*\w*\*$'
            #pattern is X*Y*Z
            pattern_second = '^\w.*\w$'
            #pattern is *X*Y*Z*
            pattern_third =  '^\*\w.*\w\*$'
            #pattern is *X*Y*Z
            pattern_fourth = '^\*\w.*\w$'
            #pattern is X*Y*Z*
            pattern_fifth = '^\w.*\w\*$'
            if re.match(pattern_first, word): #pattern is *X*
                without_star = (word[1:-1])
                new_word = without_star + '*'
                permuted_query_list.append(new_word)

            elif re.match(pattern_second, word): #pattern is X*Y*Z
                array_of_starposition = []
                for letters in range(len(word)):
                    if word[letters] == '*':
                        array_of_starposition.append(letters)
                first_star = min(array_of_starposition)
                last_star = max(array_of_starposition)
                first_slice = (word[:first_star])
                second_slice = (word[last_star+1:])
                new_word = second_slice + '$' + first_slice + '*'
                permuted_query_list.append(new_word)
            elif re.match(pattern_third, word): #pattern is *X*Y*Z*
                print(word)

            elif re.match(pattern_fourth, word):#pattern is *X*Y*Z
                permuted_words_first = []
                permuted_words_second = []
                word_list = word.split("*")
                first_part_of_query = word_list[:2]
                second_part_of_query = word_list[-1]
                first_part_of_query = first_part_of_query[1:]
                new_word_first = first_part_of_query.pop()
                for j in permuted_index_map:
                    if new_word_first in j:
                        permuted_words_first.append(j)

                new_word_second = second_part_of_query + '$' + new_word_first
                for i in permuted_words_first:
                    if new_word_second in i:
                        permuted_words_second.append(i)

                new_list = list(set(permuted_words_second) & set(permuted_words_first))
                for i in new_list:
                    i = i + '*'
                    permuted_query_list.append(i)

            elif re.match(pattern_fifth, word):#pattern is X*Y*Z*
                permuted_words_first = []
                permuted_words_second = []
                word_list = word.split("*")
                first_part_of_query = word_list[:1]
                second_part_of_query = word_list[-2]
                new_word = second_part_of_query + '$' + first_part_of_query + '*'
                permuted_query_list.append(new_word)

            else:
                print('invalid')
        # else:
    return permuted_query_list


def get_permuted_words(permuted_word, permuted_index_map):
    key_words = []
    for i in permuted_word:
        keylen = i.rfind('*')
        base = i[:keylen]
        for j in permuted_index_map:
             if base in j:
                 if base[:1] == j[:1]:
                     key_words.append(permuted_index_map[j])

    return key_words

def exhaustive_enumeration(query, key_words):
    expression = list(query.split())#the user query
    x = []
    y = []
    for word in expression:
        x.append(fnmatch.filter(key_words, word))#matches words
    y = reduce(operator.concat, x)

def get_inverted_index_values(words, inverted_index):
    documents = []
    for word in words:
        if word in inverted_index:
            doc_list = inverted_index[word]
            for i in doc_list:
                documents.append(i)

    return documents


permuted_vocabulary(inverted_index_map, permuted_index_map)
print(permuted_index_map)
query = input('\nEnter\n')
rotated_list = rotate_query(query)
word_list = get_permuted_words(rotated_list, permuted_index_map)
documents = get_inverted_index_values(word_list, inverted_index_map)
exhaustive_enumeration(query, word_list)
print("The documents are")
doc_list = list(dict.fromkeys(documents))
print(doc_list)


