"""
Найти на отрезки подотрезки с нулевой суммой
"""

def prefixsum(array):
    prefix = [0]*(len(array)+1)
    for i in range(1, len(array)+1):
        prefix[i] = prefix[i-1] + array[i-1]
    return prefix
myDict = dict()
array = list(map(int, input().split()))
for i in prefixsum(array):
    if i not in myDict:
        myDict[i] = 0
    myDict[i] += 1
print(sum([(myDict[i]*(myDict[i]-1)//2) for i in myDict.keys()])) # кол-во комбинаций 