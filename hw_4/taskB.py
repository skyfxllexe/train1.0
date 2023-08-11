import sys
s = sys.stdin.read()
s = s.replace('\n', ' ')
s = s.split(' ')

countDict = dict()
for word in s:
    if word in countDict.keys():
        if word !='':
            countDict[word] += 1
    else:
        if word != '':
            countDict[word] = 1
    if word != '':
        print(countDict[word] -1, end= ' ')
