

n,k = map(int, input().split())

arr = list(map(int, input().split()))
count = 0
array_of_prefix = [0]*(len(arr)+1)
for i in range(1,len(arr)+1):
    array_of_prefix[i] = array_of_prefix[i-1] + arr[i-1]


for i in range(len(array_of_prefix)):
    for j in range(i+1, len(array_of_prefix)):
        if array_of_prefix[j] - array_of_prefix[i] == k:
            count += 1
print(count)