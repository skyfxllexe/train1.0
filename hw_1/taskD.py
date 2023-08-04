a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
else:
    if a == 0:
        if c*c - b == 0:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        if int((c*c-b)/a) == (c*c-b) /a :
            print(int((c*c-b)/a))
        else:
            print('NO SOLUTION')