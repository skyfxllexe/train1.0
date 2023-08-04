x, y = map(int, input().split())
mode = str(input())
if mode == 'heat':
    if x < y:
        print(y)
    else:
        print(x)
if mode == 'freeze':
    if x > y:
        print(y)
    else:
        print(x)
if mode == 'auto':
    print(y)
if mode == 'fan':
    print(x)