a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if (a<=d and b<=e) or (a<=e and b<=d) or (c<=d and b<=e) or (c<=d or a<=e):
    print("YES")
else:
    print("NO")