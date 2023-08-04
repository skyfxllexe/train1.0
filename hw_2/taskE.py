n = int(input())
array = list(map(int, input().split()))
array2 = array.copy()
array2.sort(reverse=True)
winner = array2[0]
index_winner_first = 0
for i in range(len(array)):
    if array[i] == winner:
        index_winner_first = i
        break
higher = 10e5
place = 0
prev = 0
def count_elem(elem,array):
    count = 0
    for i in array:
        if elem == i:
            count += 1
    return count
for i in range(1,len(array)-1):
    if index_winner_first < i and array[i]%10 == 5 and array[i+1] < array[i] and prev < array[i]:
        for j in range(len(array2)):
            prev = array[i]
            if array2[j] == array[i]:
                place = j+1
            
        
        if count_elem(array[i], array) > 1:
            place -= count_elem(array[i], array) - 1
        if array[index_winner_first] == array[i]:
            place = 1
print(place)