first = input()
second = input()
count = 0
array1 = [first[i]+first[i-1] for i in range(len(first)-1)]
array2 = set([second[i]+second[i+1] for i in range(len(second)-1)])
for i in range(len(array1)):
    if array1[i] in array2:
        count += 1
print(count,array1)