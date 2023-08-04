

n = int(input())
f0 = int(input())
table = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    table[i][0] = a
    table[i][1] = b


    
