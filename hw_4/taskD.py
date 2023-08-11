n = int(input())
arr1 = list(map(int, input().split()))
k = int(input())
arr2 = list(map(int, input().split()))
myDict = dict()
for i in arr2:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] += 1
for i in range(len(arr1)):
    if arr1[i] < myDict[i+1]:
        print("YES")
    else:
        print("NO")