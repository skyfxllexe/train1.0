n, m, k = map(int, input().split())
array = []
for i in range(k):
    p,q = map(int, input().split())
    array.append([p-1,q-1])
table = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for s in array:
            if i == s[0] and j == s[1]:
                table[i][j] = "*"
if n == 1 and m == 1 and k == 0:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if table[i][j] != "*":
                a, b,c,d = '', '', '',''
                a1,b1,c1,d1 = '', '', '', ''
                if (n<3 or m <3):
                    if (n == 1 and m != 1):
                        if j != 0 and j != m-1:
                            a = table[0][j-1]
                            b = table[0][j+1]
                        elif j == 0:
                            a = table[0][j+1]
                        elif j == m-1:
                            a = table[0][j-1]
                    elif (m == 1 and n != 1):
                        if i != 0 and i != n-1:
                            a = table[i-1][0]
                            b = table[i+1][0]
                        elif i == 0:
                            a = table[i+1][0]
                        elif i == n-1:
                            a = table[i-1][0]
                    elif (n == 2 and m >= 2):
                        if i == 0 and j == 0:
                            a = table[i][j+1]
                            b = table[i+1][j+1]
                            c = table[i+1][j]
                        elif i == n-1 and j == 0:
                            a = table[i][j+1]
                            b = table[i-1][j]
                            c = table[i-1][j+1]
                        elif i == n- 1 and j == m-1:
                            a = table[i][j-1]
                            b = table[i-1][j]
                            c = table[i-1][j-1]
                        elif i == 0 and j == m-1:
                            a = table[i][j-1]
                            b = table[i+1][j]
                            c = table[i+1][j-1]
                        elif j > 0 and j < m-1 and i == 0:
                            a = table[i][j-1]
                            b = table[i][j+1]
                            c = table[i+1][j-1]
                            d = table[i+1][j+1]
                            a1 = table[i+1][j]
                        elif j > 0 and j < m-1 and i == 1:
                            a = table[i-1][j]
                            b = table[i-1][j+1]
                            c = table[i-1][j-1]
                            d = table[i][j-1]
                            a1 = table[i][j+1]
                    elif (m == 2 and n >= 2):
                        if i == 0 and j ==0:
                            a = table[i][j+1]
                            b = table[i+1][j]
                            c = table[i+1][j+1]
                        elif i == 0 and j == m-1:
                            a = table[i][j-1]
                            b = table[i+1][j]
                            c = table[i+1][j-1]
                        elif i == n-1 and j == m-1:
                            a = table[i][j-1]
                            b = table[i-1][j-1]
                            c = table[i-1][j]
                        elif i == n-1 and j == 0:
                            a = table[i][j+1]
                            b = table[i-1][j+1]
                            c = table[i-1][j]
                        elif i > 0 and i < n-1 and j == 0:
                            a = table[i][j+1]
                            b = table[i-1][j]
                            c = table[i-1][j+1]
                            d = table[i+1][j]
                            a1 = table[i+1][j+1]
                        elif i > 0 and i < n-1 and j == 1:
                            a = table[i][j-1]
                            b = table[i-1][j]
                            c = table[i+1][j]
                            d = table[i+1][j-1]
                            a1 = table[i-1][j-1]

                else:
                    if (i == 0 and j == 0):
                        a = table[i][j+1] # вправо
                        c = table[i+1][j] # вниз
                        a1 = table[i+1][j+1]
                    elif (i == n-1 and j == 0):
                        a = table[i][j+1] # вправо
                        d = table[i-1][j] # вверх
                        a1 = table[i-2][j+1]
                    elif (i == n-1 and j == m-1):
                        d = table[i-1][j] # вверх
                        b = table[i][j-1] # влево
                        a1 = table[i-2][j-1]
                    elif (i == 0 and j == m-1):
                        b = table[i][j-1] # влево
                        c = table[i+1][j] # вниз
                        a1 = table[i+1][j-1]
                    elif j == 0 and i>0 and i<n-1:
                        c = table[i+1][j] # вниз
                        d = table[i-1][j] # вверх
                        a = table[i][j+1] # вправо
                        a1 = table[i-1][j+1]
                        b1 = table[i+1][j+1]
                    elif j == m-1 and i>0 and i<n-1:
                        b = table[i][j-1] # влево
                        c = table[i+1][j] # вниз
                        d = table[i-1][j] # вверх
                        a1 = table[i-1][j-1]
                        b1 = table[i+1][j-1]
                    elif i == 0 and j>0 and j < m-1:
                        a = table[i][j+1] # вправо
                        b = table[i][j-1] # влево
                        c = table[i+1][j] # вниз
                        a1 = table[i+1][j-1]
                        b1 = table[i+1][j+1]
                    elif i == n-1 and j>0 and j < m-1:
                        a = table[i][j+1] # вправо
                        b = table[i][j-1] # влево
                        d = table[i-1][j] # вверх
                        a1 = table[i-1][j+1]
                        b1 = table[i-1][j-1]
                    elif j >0 and j<m-1 and i >0 and i < n-1:
                        a = table[i][j+1] # вправо
                        b = table[i][j-1] # влево
                        c = table[i+1][j] # вниз
                        d = table[i-1][j] # вверх
                        a1 = table[i+1][j-1]
                        c1 = table[i-1][j-1]
                        b1 = table[i+1][j+1]
                        d1 = table[i-1][j+1]
                temp = str(str(a)+str(b)+str(c)+str(d)+str(a1)+str(b1)+str(c1)+str(d1))
                table[i][j] += temp.count("*")

for i in range(n):
    print(*table[i])
