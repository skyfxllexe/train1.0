def BS(array, elem):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == elem:
            return array[mid]
        if array[mid] > elem:
            end = mid-1
        else:
            start = mid+1
    
    if abs(elem - array[start]) > abs(elem-array[end]):
        return array[end]
    if abs(elem - array[start]) == abs(elem-array[end]):
        return min(array[start], array[end])
    return array[start]


n,k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in arr2:
    print(BS(arr1, i))
