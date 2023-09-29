n,k = map(int, input().split())
s = input()
myDict = dict()
left = 0
maxim = -10e5
ans = 0
for right, cur_char in enumerate(s):
    if cur_char not in myDict:
        myDict[cur_char] = 0
    myDict[cur_char] += 1
    while myDict[cur_char] > k:
        myDict[s[left]] -= 1
        left += 1
    if sum(myDict.values()) > maxim:
        ans = left
        maxim = sum(myDict.values())
    
    
print(maxim, ans+1)