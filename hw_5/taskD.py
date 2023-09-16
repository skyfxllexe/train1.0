n, r = map(int, input().split())
array = list(map(int, input().split()))
second = 0
answer = 0
for i in range(n):
    while (second != n and array[second] - array[i] <= r):
        second += 1
    answer += n-second
print(answer)

