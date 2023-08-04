n = int(input())
arr = list(map(int, input().split()))
s = ''
for i in arr:
    s += str(i)

minim = 10e5
tail = ''
answer = ''
for i in range(len(s)):
    new_s = s + s[0:i][::-1]
    if new_s == new_s[::-1]:
        if len(s[0:i][::-1]) < minim:
            minim = len(s[0:i][::-1])
            tail = s[0:i][::-1]
if len(s) == 1 or s == s[::-1]:
    print(0)
else:
    print(minim)
    for i in range(len(tail)):
        answer += tail[i] + ' '
    print(answer[:-1])