
"""
Пример: AAAAABBBBBBBBBCCCCCXYAAA
Ответ: A5B9C5XYA3
"""

s = "AAZZZZZZZFFFFFBBX"
def createSet(s):
    last = s[0]
    ans = ''
    k = -1
    m = 0
    for i in range(len(s)):
        k += 1
        if s[i] != last:
            if k - m == 1:
                ans += last
            else:
                ans += last+str(k-m)  
            m = i
            last = s[i]
    if s.count(last) > 1:
        ans += last + str(s.count(last))
    else:
        ans += last
    return ans
print(createSet(s))