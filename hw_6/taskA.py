# пишу сам

def BS(array, elem):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == elem:
            return mid
        if array[mid] > elem:
            end = mid-1
        else:
            start = mid+1
    return -1


n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in arr2:
    print("YES") if BS(arr1, i) != -1 else print("NO")
