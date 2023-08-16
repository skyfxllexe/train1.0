# Дано два числа X и Y без ведущий нулей
# Необходимо проверить, можно ли получить
# первое из второго перестановкой цифр

x, y = map(str, input().split())
mX, mY = dict(), dict()
for i in x:
    if i in mX:
        mX[i] += 1
    else:
        mX[i] = 1
for i in y:
    if i in mY:
        mY[i] += 1
    else:
        mY[i] = 1
print(mX == mY)