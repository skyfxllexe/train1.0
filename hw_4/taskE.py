n = int(input())

pyraDict = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a in pyraDict.keys() and pyraDict[a] < b:
        pyraDict[a] = b
    elif a not in pyraDict.keys():
        pyraDict[a] = b
print(sum(pyraDict.values()))
