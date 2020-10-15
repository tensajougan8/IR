import re
import os

def inverted_index(words, map, path):
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
        nonstemmedwords(words, f, map)


def nonstemmedwords(words, f, map):
    for i in words:
        list = []
        if i != '':
            if i in map.keys():
                list1 = map[i]
                g = 'D' + str(f + 1) + '.txt'
                if list1.count(g) > 0:
                    pass
                else:
                    list1.append(g)
            else:
                g = 'D' + str(f + 1) + '.txt'
                list.append(g)
                map[i] = list
        else:
            pass