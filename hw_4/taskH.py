
g, s = map(int, input().split())
s1 = input()
s2 = input()
count = 0

myDict1 = dict()
for i in s1:
    if i not in myDict1:
        myDict1[i] = 0
    myDict1[i] += 1
for i in range(len(s2)-len(s1)+1):
    curDict = dict()
    part = s2[i:len(s1)+i]
    for j in part:
        if j not in curDict:
            curDict[j] = 0
        curDict[j] += 1
    if curDict == myDict1:
        count += 1
print(count)

