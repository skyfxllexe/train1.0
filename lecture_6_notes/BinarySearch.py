# пишу сам

def BS(array, elem):
    start = 0
    end = len(array)
    while start < end:
        mid = (start+end)//2
        if array[mid] == elem:
            return mid
        if array[mid] > elem:
            end = mid
        else:
            start = mid
    return "Not found"
array = [1,5,9,15,16]
print(BS(array, 16))