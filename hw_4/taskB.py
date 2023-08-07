import sys
s = sys.stdin.read()
s = s.replace('\n', ' ')
s = s.split(' ')

countDict = dict()
for word in s:
    if word in countDict.keys():
        countDict[word] += 1
    else:
        countDict[word] = 1

    print(countDict[word] -1, end= ' ')
