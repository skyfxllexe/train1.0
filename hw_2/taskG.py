array = list(map(int, input().split()))
# Инициализация двух переменных для хранения наибольших чисел
max1 = max2 = float('-inf')
min1 = min2 = float('inf')
# Проходим по списку чисел и обновляем значения наибольших чисел
for num in array:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num
if max1*max2 > min1*min2:
    print(min(max1, max2), max(max1,max2))
else:
    print(min(min1, min2), max(min1,min2))
# Пример использования функции


