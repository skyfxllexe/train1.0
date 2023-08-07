lang = []


n = int(input())
array2 = [[0 for _ in range(1)] for _ in range(n)]
for i in range(n):
    m = int(input())
    array = []
    for j in range(m):
        lan = input()
        array.append(lan)
        lang.append(lan)
    array2[i] = array

all_intersection = set()
prev = set(array2[0])
for i in range(len(array2)-1):
    all_intersection = set(array2[i]) & set(array2[i+1]) & prev
    prev = all_intersection
print(len(all_intersection))
for i in all_intersection:
    print(i)
print(len(set(lang)))
for i in set(lang):
    print(i)