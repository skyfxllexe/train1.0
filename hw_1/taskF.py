a, b, c, d = map(int, input().split())

s1 = [(b+c)*max(a,d), b+c, max(a,d)]
s2 = [(b+d)*max(a,c), b+d, max(a,c)]
s3 = [(a+c)*max(b,d), a+c, max(b,d)]
s4 = [(a+d)*max(b,c), a+d, max(b,c)]
minimS = 10e10
array = 0
for i in [s1,s2,s3,s4]:
    if i[0] <= minimS:
        minimS = i[0]
        array = i
print(array[1], array[2])