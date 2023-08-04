import math
array = list(map(int, input().split()))


maxP1, maxP2, maxP3 = -10e100,-10e100,-10e100
minM1, minM2 = 10e100, 10e100

for num in array:
    if num > maxP1:
        maxP3 = maxP2
        maxP2 = maxP1
        maxP1 = num
    elif num> maxP2:
        maxP3 = maxP2
        maxP2 = num
    elif num > maxP3:
        maxP3 = num
    if num < minM1:
        minM2 = minM1
        minM1 = num
    elif num < minM2:
        minM2 = num
arr = [maxP1, maxP2, maxP3, minM1, minM2]

ver1 = [maxP1 * minM1 * minM2, [maxP1, minM1, minM2]]
ver2 = [maxP1 * maxP2 * maxP3, [maxP1, maxP2, maxP3]]
maxim = -10e100
data = 0
for i in [ver1,ver2]:
    if i[0] > maxim:
        maxim = i[0]
        data = i[1]
print(*data)