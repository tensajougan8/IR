import re
import os

def initial_index(words, map, path):
    files = []
    d = path
    for r, d, f in os.walk(d):
        for h in f:
            if '.txt' in h:
                files.append(os.path.join(r, h))

    for f in range(len(files)):
        file = open(files[f], 'r')
        text = file.read().lower()

        words = re.split(r'\W+', text)
        count = 0
        nonstemmedwords(words, f, map, count)
        count +=1


def nonstemmedwords(words, f, map, count):
    for i in words:
        list = []
        if i != '':
            if i in map.keys():
               
            else:

        else:
            pass
words = []
map = dict()
path = r"C:\Users\Valdo\Desktop\test\permuted"
initial_index(words,map,path)
print(map)