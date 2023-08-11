s = "azxxzy"
answer=  ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        answer += '?'
    else:
        answer += s[i]
print(answer)