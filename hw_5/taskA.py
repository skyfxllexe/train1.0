n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
i, j = 0, 0
minim = 10e100
answer1, answer2 = 0, 0
while i < len(arr1) and j < len(arr2):
    if arr2[j]- arr1[i] == 0:
        answer1, answer2 = arr2[j], arr1[i]
        break
    if arr2[j] - arr1[i] < minim:
        minim = abs(arr2[j] - arr1[i])
        answer1, answer2 = arr2[j], arr1[i]
    if arr2[j] < arr1[i]:
        j += 1
    else:
        i += 1
print(answer1, answer2)