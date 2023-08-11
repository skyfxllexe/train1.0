import sys

s = sys.stdin.read()
s=s.split('\n')
s = s[:-1]
myDict = dict()
for i in range(len(s)):
    s[i] = s[i].split(' ')

for i in range(len(s)):
    if s[i][0] == 'DEPOSIT' and s[i][1] not in myDict:
        myDict[s[i][1]] = int(s[i][2])
    elif s[i][0] == 'DEPOSIT' and s[i][1] in myDict:
        myDict[s[i][1]] += int(s[i][2])
    elif s[i][0] == 'TRANSFER':
        if s[i][2] in myDict and s[i][1] in myDict:
            myDict[s[i][2]] += int(s[i][3])
            myDict[s[i][1]] -= int(s[i][3])
        elif s[i][2] not in myDict and s[i][1] in myDict:
            myDict[s[i][2]] = int(s[i][3])
            myDict[s[i][1]] -= int(s[i][3])
        elif s[i][2] in myDict and s[i][1] not in myDict:
            myDict[s[i][2]] += int(s[i][3])
            myDict[s[i][1]] = -int(s[i][3])
        elif s[i][2] not in myDict and s[i][1] not in myDict:
            myDict[s[i][1]] = -int(s[i][3])
            myDict[s[i][2]] = int(s[i][3])
    elif s[i][0] == 'WITHDRAW' and s[i][1] in myDict:
        myDict[s[i][1]] -= int(s[i][2])
    elif s[i][0] == 'WITHDRAW' and s[i][1] not in myDict:
        myDict[s[i][1]] = -int(s[i][2])
    elif s[i][0] == 'BALANCE' and s[i][1] in myDict:
        print(myDict[s[i][1]])
    elif s[i][0] == 'BALANCE' and s[i][1] not in myDict:
        print('ERROR')
    elif s[i][0] == 'INCOME':
        for j in myDict:
            if myDict[j] > 0:
                myDict[j] += myDict[j]*int(s[i][1])//100


