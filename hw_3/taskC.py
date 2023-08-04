n, m = map(int, input().split())
array1 = [int(input()) for _ in range(n)] # аня
array2 = [int(input()) for _ in range(m)] # боря
a = len(set(array1)&set(array2))
b = sorted(list(set(array1)&set(array2)))
c = sorted(set(array1).difference(set(array1)&set(array2)))
d = sorted(set(array2).difference(set(array1)&set(array2)))
print('--')
print(a)
print(*b)
print(len(c))
print(*c)
print(len(d))
print(*d)