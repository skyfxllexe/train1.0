n, k, m = map(int, input().split())
if n == 0 or k == 0 or m == 0 or m>k or m>n:
	print(0)
else:
	result = 0
	while n>=k:
		l = n//k # количество заготовок
		n -= k*l - l*(k%m) # забираем с заготовок, добавляем с деталей
		result += l*(k//m) # в результат добавляем количество заготовок на k // m, k // m = количество деталей с 1 заготовки
	print(result)
