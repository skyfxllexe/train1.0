array = set(list(map(int, input().split())))
print(len(set([int(i) for i in input()]).difference(array)))