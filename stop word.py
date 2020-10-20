import os
import re
words = []
map = dict()
stopwords = []
results = dict()

class stopWord:
    word = []
    count = 0


    def wordmatrix(words,map,stopwords):
        files = []
        d = r"C:\Users\Valdo\Desktop\test\st"
        for r, d, f in os.walk(d):
            for file in f:
                if 'stopwords.txt' in file:
                    file1 = os.path.join(r, file)
                    g = open(file1,'r')
                    for word in g.read().split():
                        stopwords.append(word)
                    # stopwords = g.read().lower()
                    # stopwords = re.split(r'\W+',stopwords)

                else:
                    files.append(os.path.join(r, file))

        count = 0

        for f in files:
            file = open(f, 'r')
            text = file.read().lower()
            words = re.split(r'\W+', text)
            obj.withstopwords(words, files, count)
            count += 1



    def withstopwords(words, files, count):
        for i in words:
            list = []
            if i != '':
                if i in map.keys():
                    list1 = map[i]
                    g = 'D' + str(count+1) + '.txt'
                    if list1.count(g) > 0:
                        pass
                    else:
                        list1.append(g)
                else:
                    g = 'D' + str(count+1) + '.txt'
                    list.append(g)
                    map[i] = list
            else:
                pass

    def matrix(stopwords,map):
        for i in stopwords:
            if i in map.keys():
               del map[i]
            else:
                pass



    def checkword(expression):
        for key in expression:
            if key in map.keys():
                pass
            else:
                print(key,"is an invalid word or word does not exist ")
                return False

obj = stopWord
obj.wordmatrix(words,map,stopwords)
d = r"C:\Users\Valdo\Desktop\test\index.txt"
with open(d,'w') as data:
    data.write(str(map))

print("File written")
obj.matrix(stopwords,map)
print(map)
# print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Key','D1','D2','D3','D4','D5','D6'))
# for k, v in results.items():
#     d1, d2, d3, d4, d5, d6 = v
#     print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(k, d1, d2, d3, d4, d5, d6))
# print("\n")
# # print(map)
#
# print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Key','D1','D2','D3','D4','D5','D6'))
# for k, v in map.items():
#     d1, d2, d3, d4, d5, d6 = v
#     print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(k, d1, d2, d3, d4, d5, d6))

expression = input("Enter\n")
expression = list(expression.split())
exp = obj.checkword(expression)
newlist = []
if exp == False:
    expression = input("Enter\n")
    expression = list(expression.split())
    exp = obj.checkword(expression)
else:
    for i in expression:
        if i in map.keys():
            if len(newlist) == 0:
                newlist = map[i]
            else:
                list2 = map[i]
                for i in list2:
                    newlist.append(i)

new = list(dict.fromkeys(newlist))
print(new)


