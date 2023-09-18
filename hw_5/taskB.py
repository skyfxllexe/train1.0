
n,k = map(int, input().split())

arr = list(map(int, input().split()))
count = 0
array_of_prefix = [0]*(len(arr)+1)
for i in range(1,len(arr)+1):
    array_of_prefix[i] = array_of_prefix[i-1] + arr[i-1]


i = 0
j = 1
answer = 0
while j < len(array_of_prefix) and i < len(array_of_prefix):
    if array_of_prefix[j] - array_of_prefix[i] == k:
        i += 1
        j += 1
        answer += 1
    elif array_of_prefix[j] - array_of_prefix[i] > 17:
        i += 1
    else:
        j += 1
    
    


print(answer)