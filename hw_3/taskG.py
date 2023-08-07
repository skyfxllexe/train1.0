n = int(input())
count = 0
usedBefore = set()
for i in range(n):
    a,b = map(int, input().split())
    if a+b == n-1 and a >= 0 and b >= 0:
        usedBefore.add(a)

print(len(usedBefore))