import re
import os, glob
import math

def initial_index(path, vectormap, query, query1, docmap):
    files = []
    folder_path = path
    filecount = 0
    for r, path, f in os.walk(path):
        for h in f:
            if '.txt' in h:
                filecount +=1
    word = list(query1.split())
    expression = list(query.split())
    No_of_collection = filecount
    R = len(expression)
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):

        with open(filename, 'r') as f:
            text = f.read().lower()
            tempwords = re.split(r'\W+', text)
            print(tempwords)
            for one_word in word:
                head, tail = os.path.split(filename)
                tail, head = tail.split('.')
                if one_word in tempwords and tail in expression:
                    if one_word in vectormap.keys():
                        x = vectormap[one_word]
                        y = x[2] + 1
                        y2 = x[3] + 1
                        x[2] = y
                        x[3] = y2
                        vectormap[one_word] = x
                        list_of_words = []
                        if tail in docmap.keys():
                            list_of_words = docmap[tail]
                            list_of_words.append(one_word)
                            docmap[tail] = list_of_words
                        else:
                            list_of_words.append(one_word)
                            docmap[tail] = list_of_words
                    else:
                        x = [No_of_collection, R, 1, 1]#format is [N,R,n,r]
                        vectormap[one_word] = x
                        list_of_words = []
                        if tail in docmap.keys():
                            list_of_words = docmap[tail]
                            list_of_words.append(one_word)
                            docmap[tail] = list_of_words
                        else:
                            list_of_words.append(one_word)
                            docmap[tail] = list_of_words
                elif one_word in tempwords:
                    if one_word in vectormap.keys():
                        x = vectormap[one_word]
                        y = x[2] + 1
                        x[2] = y
                        vectormap[one_word] = x
                    else:
                        x = [No_of_collection, R, 1, 0]#format is [N,R,n,r]
                        vectormap[one_word] = x
                        list_of_words = []
                        if tail in docmap.keys():
                            list_of_words = docmap[tail]
                            list_of_words.append(one_word)
                            docmap[tail] = list_of_words
                        else:
                            list_of_words.append(one_word)
                            docmap[tail] = list_of_words

def calculate_weights_of_terms(vectormap):
    for key in vectormap.keys():
        x = vectormap[key]
        N = x[0]
        n = x[2]
        R = x[1]
        r = x[3]
        w1 = math.log(((r + 0.5) / (R + 1))/((n + 1) / (N + 2)), 10)
        w1 = math.floor(w1 * 10 ** 3) / 10 ** 3
        w2 = math.log(((r + 0.5)/(R + 1))/((n - r + 0.5)/(N - R + 1)), 10)
        w2 = math.floor(w2 * 10 ** 3) / 10 ** 3
        w3 = math.log(((r + 0.5)/(R - r + 0.5))/((n + 1)/(N - n + 1)), 10)
        w3 = math.floor(w3 * 10 ** 3) / 10 ** 3
        w4 = math.log(((r + 0.5)/(R - r + 0.5))/((n - r + 0.5)/(N - n - (R - r))), 10)
        w4 = math.floor(w4 * 10 ** 3) / 10 ** 3
        x = [w1, w2, w3, w4]
        vectormap[key] = x
def calculate_weights_for_doc(vectormap, docmap, resultmap):
    for key in docmap.keys():
        for value in docmap[key]:
            if value in vectormap.keys():
                if value in resultmap.keys():
                    x = resultmap[value]
                    x1 = vectormap[value]
                    y = []
                    for index,x in enumerate(x):
                        j = x[index] + x1[index]
                        y.append(j)
                else:
                    x = vectormap[value]
                    resultmap[key] = x

words = []
normalization_list = []
vectormap = dict()
docmap = dict()
resultmap = dict()
path = r"C:\Users\Valdo\Desktop\test\cosine"
query = input('\nEnter relevant document\n')
query1 = input('\nEnter relevant document\n')
initial_index(path, vectormap, query, query1, docmap)
print(vectormap)
print(docmap)
calculate_weights_of_terms(vectormap)
calculate_weights_for_doc(vectormap, docmap, resultmap)
print(resultmap)