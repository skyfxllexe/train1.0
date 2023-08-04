a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if (a*d-b*c):
    det = a*d-b*c
    x0 = (e*d-b*f)/det
    y0 =(a*f-c*e)/det
    print(2, x0, y0)
else:
    if (a == 0 and c == 0):
        if b != 0 and d != 0:
            if (e/b == f / d):
                print(4, e/b)
                print('hi')
            else:
                print(0)
        elif b == 0 and d!= 0:
            print(4, f/d)
        elif b != 0 and d == 0:
            print(4, e/b)
    elif (b == 0 and d == 0):
        if a !=0 and c!= 0:
            if (e/a == f/c):
                print(4, e/a)
            else:
                print(0)
        elif a == 0 and c!= 0:
            print(3, f/c)
        elif a != 0 and c ==0:
            print(3, e/a)
    elif (c/d == a/b):
        if (e/b == f/d):
            print(1, -c/d, f/d)
        else:
            print(0)
    
    elif (a == 0 and b == 0):
        print(1, -c/d, f/d)
    elif (c == 0 and d == 0):
        print(1, -a/e, e/b)
if (a == 0 and b ==0 and c ==0 and d ==0 and e == 0 and f ==0):
    print(5)
