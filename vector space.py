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
    res = list(map.keys())[0]
    x = map[str(res)]
    len_of_list = len(x)
    for i in map.keys():
        x = map[i]
        df = len_of_list - x.count(0)
        idf = math.log(len_of_list/df, 10)
        idf = math.floor(idf * 10 ** 2) / 10 ** 2
        idfmap[i] = idf

def idf_table(idftablemap, idfmap):
    for i in idfmap.keys():
        for j in idftablemap.keys():
            if i == j:
                y = []
                x = idftablemap[j]
                for value in x:
                    h = value * idfmap[i]
                    y.append(h)
                idftablemap[i] = y
            else:
                pass

def idftable_with_query(query, idfmap , querymap):
    expression = list(query.split())
    for i in expression:
        tempcount = 0
        for j in expression:
            if i == j:
                tempcount += 1
            else:
                pass
        querymap[i] = tempcount


    for i in querymap.keys():
        for j in idfmap.keys():
            if i == j:
                y = querymap[i] * idfmap[j]
                x = idftablemap[i]
                x.append(y)
            else:
                pass

def calculate_similarity_coeff(map, idftablemap, querymap):
    res = list(map.keys())[0]
    x = map[str(res)]
    len_of_list = len(x)
    query_index = len_of_list+1
    h = []
    temp = dict()
    for index in range(len_of_list):
        y = 0
        for j in querymap:
            x = idftablemap[j]
            y += x[index] * x[len_of_list]
        y = math.floor(y * 10 ** 4) / 10 ** 4
        temp[y] = 'D' + str(index+1) + '.txt'
        h.append(y)
        print("Similarity coefficeint for D"+str(index+1)+" is",y)
    for elm in sorted(temp.items(),reverse=True):
        print("the docs are",elm[1],"the coeeficient are",elm[0])


words = []
vectormap = dict()
idfmap = dict()
idftablemap = dict()
querymap = dict()
path = r"C:\Users\Valdo\Desktop\test\vector"
initial_index(path, vectormap)
print(vectormap)
find_idf(vectormap, idfmap)
idftablemap = vectormap.copy()
idf_table(idftablemap, idfmap)
print(idftablemap)
query = input('\nEnter\n')
idftable_with_query(query, idfmap, querymap)
print(idftablemap)
calculate_similarity_coeff(vectormap, idftablemap, querymap)
