import sys
s = sys.stdin.read()
s = s.replace('\n', ' ')
s = s.split(' ')
wordDict = dict()

for i in s:
    if i in wordDict.keys():
        wordDict[i] += 1
    else:
        if i != '':
            wordDict[i] = 1
setOfMaxims = set()
maxim = max(wordDict.values())
for i in wordDict.keys():
    if wordDict[i] == maxim:
        setOfMaxims.add(i)
print(min(setOfMaxims))