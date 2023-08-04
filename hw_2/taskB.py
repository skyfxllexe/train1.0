array = []
while True:
	a = int(input())
	if a == -2000000000:
		break
	array.append(a)
CONSTANT = True
ASCENDING = True
WEAKLY_ASCENDING = False
DESCENDING = True
WEAKLY_DESCENDING = False
RANDOM = True

for i in range(len(array)-1):
	if array[i] != array[i+1]:
		CONSTANT = False
	if array[i] > array[i+1]:
		ASCENDING = False
	if array[i] < array[i+1]:
		DESCENDING = False
# для WEAKLY_ASCENDING
if not(CONSTANT):
	if ASCENDING:
		for i in range(len(array)-1):
			if array[i] == array[i+1]:
				WEAKLY_ASCENDING = True
				ASCENDING = False
				RANDOM = False
				break
		if ASCENDING:
			RANDOM = False
	elif DESCENDING:
		for i in range(len(array)-1):
			if array[i] == array[i+1]:
				WEAKLY_DESCENDING = True
				DESCENDING = False
				RANDOM = False
				break
		if DESCENDING:
			RANDOM = False
if CONSTANT:
	ASCENDING = False
	WEAKLY_ASCENDING = False
	DESCENDING = False
	WEAKLY_DESCENDING = False
	RANDOM = False

arr = [CONSTANT, ASCENDING,WEAKLY_ASCENDING, DESCENDING, WEAKLY_DESCENDING, RANDOM]
names = ["CONSTANT", "ASCENDING", "WEAKLY ASCENDING", "DESCENDING", "WEAKLY DESCENDING", "RANDOM"]

for i,j in zip(arr, names):
	if i == True:
		print(j)