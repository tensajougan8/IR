import re
import os
import math

def initial_index(path, vectormap):
    files = []
    d = path
    filecount = 0
    for r, d, f in os.walk(d):
        for h in f:
            if '.txt' in h:
                files.append(os.path.join(r, h))
                filecount +=1

    count = 0
    for f in range(len(files)):
        file = open(files[f], 'r')
        text = file.read().lower()

        tempwords = re.split(r'\W+', text)

        nonstemmedwords(tempwords, words, vectormap, count, filecount)
        count +=1 #to keep track of document no which will act as an index


def nonstemmedwords(tempwords, words, map, index, filecount):
    for i in tempwords:
        new_list = []
        for k in range(filecount):
            new_list.append(0)
        tempcount = 0
        for j in tempwords:
            if i == j:
                tempcount +=1
            else:
                pass
        if i in map.keys():
            y = map[i]
            y[index] = tempcount
            map[i] = y
        else:
            new_list[index] = tempcount
            map[i] = new_list


def find_idf(map, idfmap):#finding the idf of a term and storing it in a document
    for i in map.keys():
        x = map[i]
        j = []
        for value in x:
            if value == 0:
                j.append(value)
            else:
                idf = 1 + math.log(value, 10)
                idf = math.floor(idf * 10 ** 3) / 10 ** 3
                j.append(idf)
        idfmap[i] = j

def normalization(idfmap, idftablemap, normalization_list):
    res = list(idfmap.keys())[0]
    x = idfmap[str(res)]
    len_of_list = len(x)
    for i in range(len_of_list):
        y = 0
        for key in idfmap.keys():
            x = idfmap[key]
            j = x[i]
            j = j * j
            y = y + j
        y = math.sqrt(y)
        normalization_list.append(y)#makes list of the values ffor D1 ....Dn
    for key in idfmap.keys():
        j = []
        for i in range(len_of_list):
            x = idfmap[key]
            y = x[i]/normalization_list[i]
            y = math.floor(y * 10 ** 3) / 10 ** 3
            j.append(y)
        idftablemap[key] = j

def idftable_with_query(query, idftablemap, querymap):
    expression = list(query.split())
    new_list = []
    for i in expression:#loop for counting the repeats in the query
        tempcount = 0
        for j in expression:
            if i == j:
                tempcount += 1
            else:
                pass
        new_list.append(tempcount)
        querymap[i] = tempcount
    y = 0
    for value in new_list:
        if value == 0:
            pass
        else:
            idf = 1 + math.log(value, 10)
            idf = math.floor(idf * 10 ** 3) / 10 ** 3
            idf = idf * idf
            y = idf + y

    y = math.sqrt(y)
    y = math.floor(y * 10 ** 3) / 10 ** 3

    for key in querymap.keys():
        x = querymap[key]
        x = x/y
        x = math.floor(x * 10 ** 3) / 10 ** 3
        for j in idftablemap.keys():
            if j == key:
                r = idftablemap[key]
                r.append(x)
                idftablemap[key] = r

def calculate_cosine(map, idftablemap, querymap):
    res = list(map.keys())[0]
    x = map[str(res)]
    len_of_list = len(x)
    query_index = len_of_list + 1
    h = []
    temp = dict()
    for index in range(len_of_list):
        y = 0
        for j in querymap:
            x = idftablemap[j]
            y += x[index] * x[len_of_list]
        y = math.floor(y * 10 ** 4) / 10 ** 4
        temp[y] = 'D' + str(index + 1) + '.txt'
        h.append(y)
        print("Similarity coefficeint for D" + str(index + 1) + " is", y)
    for elm in sorted(temp.items(), reverse=True):
        print("the docs are", elm[1], "the coeeficient are", elm[0])

words = []
normalization_list = []
vectormap = dict()
idfmap = dict()
idftablemap = dict()
querymap = dict()
path = r"C:\Users\Valdo\Desktop\test\cosine"
initial_index(path, vectormap)
print(vectormap)
find_idf(vectormap, idfmap)
print(idfmap)
normalization(idfmap,idftablemap, normalization_list)
print(idftablemap)
query = input('\nEnter\n')
idftable_with_query(query, idftablemap, querymap)
calculate_cosine(vectormap, idftablemap, querymap)