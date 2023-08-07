n = int(input())
synonym = dict()
for i in range(n):
    a, b = map(str, input().split())
    synonym[a] = b
    synonym[b] = a
syn = input()
print(synonym[syn])
