from itertools import permutations
g, s = map(int, input().split())
s1 = input()
s2 = input()
set1 = set()
count = 0
for i in permutations(s1):
    set1.add(''.join(i))
    
for i in set1:
    for j in range(len(s2)-len(i)+1):
        if s2[j:len(i)+j] == i:
            count += 1
print(count)


