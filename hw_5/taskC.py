
n = int(input())
arrayN = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
arrayM = [list(map(int, input().split())) for _ in range(m)]

for i in range(len(arrayM)):
    result = 0
    for j in range(1,len(arrayN[arrayM[i][0]-1:arrayM[i][1]+1])):
        if arrayN[j-1] < arrayN[j]:
            result += abs(arrayN[j-1]-arrayN[j])
    print(result)