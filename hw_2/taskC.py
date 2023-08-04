from random import randint
n = int(input())
array = list(map(int, input().split()))
x = int(input())
minim = 10e5
index = 0
for i in range(len(array)):
    if abs(x-array[i]) < minim:
        minim = abs(x-array[i])
        index = i
if x > array[index]:
    print(x - minim)
else:
    print(x + minim)
