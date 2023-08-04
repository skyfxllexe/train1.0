import sys
s = sys.stdin.read()
s = s.replace('\n', ' ')
arr = []
start = 0
for i in range(1,len(s)):
    if s[i] == ' ' and s[i-1]!= ' ':
        arr.append(s[start:i])
    elif s[i] != ' ' and s[i-1] == ' ':
        start = i
print(len(set(arr)))