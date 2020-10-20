# This program is for Term Document Incidence Matrix

import os
import re

word = []
count = 0
map = dict()

d = r"C:\Users\Valdo\Desktop\test\TM"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(d):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
            count += 1

print('The number of files with .txt extension are', count)

for f in files:
    file = open(f, 'r')
    # .lower() returns a version with all upper case characters replaced with lower case characters.
    text = file.read().lower()
    #file.close()
    # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
    text = re.sub('[^a-z\ \']+', " ", text)
    words = list(text.split())
    for x in words:
        word.append(x)

# Removes dupliates from the list
word = list(dict.fromkeys(word))
for key in word:
    lst = []
    for f in files:
        file = open(f, 'r')
        text = file.read().lower()
        # fo = re.search(r'\b' + key + '\W', text)
        if (f' {key} ' in f' {text} '): #(' ' + key + ' ') in (' ' + text + ' '):
            lst.append(1)
        else:
            lst.append(0)
    map[key] = lst

# print(map)
print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Key','D1','D2','D3','D4','D5','D6'))
for k, v in map.items():
    d1, d2, d3, d4, d5, d6 = v
    print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(k, d1, d2, d3, d4, d5, d6))

#Stack
precedence ={"NOT": 3, "AND": 2, "OR": 1}
op = ['AND', 'OR', 'NOT']
operand = []
operator = []

def andFunc(operand , map):
    a = operand.pop()
    b = operand.pop()
    if type(a) == str:
        z = map[a]
    else:
        z = a
    if type(b) == str:
        z1 = map[b]
    else:
        z1 = b
    print('\n')
    print(z)
    print(z1)
    g = [z and z1 for z, z1 in zip(z, z1)]
    print("After AND operation the result is")
    print(g)
    return(g)

def notFunc(operand, map):
    a = operand.pop()
    if type(a) == str:
        z = map[a]
    else:
        z = a
    g = []
    for i in z:
        if i == 1:
            g.append(0)
        else:
            g.append(1)
    print('\n')
    print("After NOT operation the result is")
    print(g)
    return(g)

def orFunc(operand, map):
    a = operand.pop()
    b = operand.pop()
    if type(a) == str:
        z = map[a]
    else:
        z = a
    if type(b) == str:
        z1 = map[b]
    else:
        z1 = b
    print('\n')
    print(z)
    print(z1)
    g = [z or z1 for z, z1 in zip(z, z1)]
    print("After OR operation the result is")
    print(g)
    return g

expression = input("Enter\n")
expression = list(expression.split())
r = len(expression) - 1
iterate = 0
for i in expression:
    if i in map.keys():
        if iterate == r:
            operand.append(i)
            while len(operand) != 1:
                y = operator.pop()
                if y == 'OR':
                    p = orFunc(operand, map)
                    operand.append(p)
                elif y == 'AND':
                    p = andFunc(operand, map)
                    operand.append(p)
                elif y == 'NOT':
                    p = notFunc(operand, map)
                    operand.append(p)
        else:
            operand.append(i)
    elif i in op:
        if len(operator) == 0:
            operator.append(i)
        else:
            precedenceValue1 = precedence.get(i)
            j = operator[-1]
            precedenceValue2 = precedence.get(j)
            if j == '(':
                operator.append(i)

            elif precedenceValue1 >= precedenceValue2:
                operator.append(i)

            else:
                while precedenceValue1 < precedenceValue2:
                    y = operator.pop()
                    if y == 'OR':
                        p = orFunc(operand, map)
                        operand.append(p)
                    elif y == 'AND':
                        p = andFunc(operand, map)
                        operand.append(p)
                    elif y == 'NOT':
                        p = notFunc(operand, map)
                        operand.append(p)
                    precedenceValue1 = precedence.get(i)
                    if len(operator) > 0:
                        j = operator[-1]
                        precedenceValue2 = precedence.get(j)
                    else:
                        operator.append(i)
                        break
    elif i == '(':
        operator.append(i)
    elif i == ')':
        j = operator[-1]
        while j != '(':
            y = operator.pop()
            if y == 'OR':
                p = orFunc(operand, map)
                operand.append(p)
            elif y == 'AND':
                p = andFunc(operand, map)
                operand.append(p)
            elif y == 'NOT':
                p = notFunc(operand, map)
                operand.append(p)
            j = operator[-1]
        if iterate == r:
            while len(operand) != 1:
                y = operator.pop()
                if y == 'OR':
                    p = orFunc(operand, map)
                    operand.append(p)
                elif y == 'AND':
                    p = andFunc(operand, map)
                    operand.append(p)
                elif y == 'NOT':
                    p = notFunc(operand, map)
                    operand.append(p)
    iterate += 1

j = operand.pop()
print(j)
