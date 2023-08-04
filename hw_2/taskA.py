array = list(map(int, input().split()))
flag = "YES"
for i in range(len(array)-1):
	if array[i] >= array[i+1]:
		flag = "NO"
print(flag)