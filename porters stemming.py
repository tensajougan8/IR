import os
import re
from inverted_index import *

words = []
outputlist = []
map = dict()


class stemming:

    def vowel(last_char):
        if last_char == 'a':
            return True
        elif last_char == 'e':
            return True
        elif last_char == 'i':
            return True
        elif last_char == 'o':
            return True
        elif last_char == 'u':
            return True
        else:
            return False

#Applying the algorithm on the map
    def stemmwords(map):
        key_copy = tuple(map.keys())
        for key in key_copy:
            if key.endswith('sses'):
                originalsuffix = 'sses'
                replacesuffix = 'ss'
                new_key = obj.replacekey(key,originalsuffix,replacesuffix)
                if new_key in map.keys():
                    temp = map[new_key]
                    temp2 = map[key]
                    temp3 = temp + temp2
                    map.pop(key)
                    map[new_key] = temp3
                else:
                    map[new_key] = map.pop(key)
            elif key.endswith('ies'):
                originalsuffix = 'ies'
                replacesuffix = 'i'
                new_key = obj.replacekey(key,originalsuffix,replacesuffix)
                if new_key in map.keys():
                    temp = map[new_key]
                    temp2 = map[key]
                    temp3 = temp + temp2
                    map.pop(key)
                    map[new_key] = temp3
                else:
                    map[new_key] = map.pop(key)
            elif key.endswith('ss'):
                originalsuffix = 'ss'
                replacesuffix = 'ss'
                new_key = obj.replacekey(key,originalsuffix,replacesuffix)
                if new_key in map.keys():
                    temp = map[new_key]
                    temp2 = map[key]
                    temp3 = temp + temp2
                    map.pop(key)
                    map[new_key] = temp3
                else:
                    map[new_key] = map.pop(key)
            elif key.endswith('s'):
                originalsuffix = 's'
                new_key = obj.checkvowel(key,originalsuffix)
                map[new_key] = map.pop(key)
            else:
                pass

#Replace the word
    def replacekey(key,originalsuffix,replacesuffix):
        keylen = key.rfind(originalsuffix)
        base = key[:keylen]
        base += replacesuffix
        return base

    def checkvowel(key,originalsuffix):
        keylen = key.rfind(originalsuffix)
        base = key[:keylen]
        last_char = base[keylen-1]
        vowel = obj.vowel(last_char)
        if vowel == True:
            return key
        else:
            return base

    def finalresults(key, outputlist):
        if key in map.keys():
            newlist = map[key]
            for i in newlist:
                outputlist.append(i)
        else:
            print(key, "is in invalid word")
            return False

#Applying the porters algorithm on the query
    def checkquery(query):
        for words in query:
            if words.endswith('sses'):
                originalsuffix = 'sses'
                replacesuffix = 'ss'
                new_key = obj.replacekey(words, originalsuffix, replacesuffix)
                new_keylist = obj.finalresults(new_key, outputlist)
            elif words.endswith('ies'):
                originalsuffix = 'ies'
                replacesuffix = 'i'
                new_key = obj.replacekey(words, originalsuffix, replacesuffix)
                new_keylist = obj.finalresults(new_key,outputlist)
            elif words.endswith('ss'):
                originalsuffix = 'ss'
                replacesuffix = 'ss'
                new_key = obj.replacekey(words, originalsuffix, replacesuffix)
                new_keylist = obj.finalresults(new_key,outputlist)
            elif words.endswith('s'):
                originalsuffix = 's'
                new_key = obj.checkvowel(words, originalsuffix)
                new_keylist = obj.finalresults(new_key,outputlist)
            elif words in map.keys():
                new_keylist = obj.finalresults(words, outputlist)
            else:
                print(words,"is in invalid query")
                return False


obj = stemming
path = r"C:\Users\Valdo\Desktop\test\stemming"
#Module imported and the function inverted index is used
inverted_index(words,map,path)
print(map)
# d = r"C:\Users\Valdo\Desktop\test\stemming\index1.txt"
# with open(d,'w') as data:
#     data.write(str(map))

obj.stemmwords(map)
print(map)
# d = r"C:\Users\Valdo\Desktop\test\stemming\index2.txt"
# with open(d,'w') as data:
#     data.write(str(map))

expression = input("Enter\n")
query = list(expression.split())
results = obj.checkquery(query)

if results == False:
    print("So it's an invalid query")
else:
    new = list(dict.fromkeys(outputlist))
    print(new)
