n = int(input())

myDict = dict()
for i in range(n):
    word = input()
    if word.lower() not in myDict:
        myDict[word.lower()] = []
    myDict[word.lower()].append(word)

string = input()
count = 0 
for i in string.split():
    suma = 0
    for j in i:
        if j.isupper():
            suma += 1
    if suma > 1:
        count += 1
    if i.lower() not in myDict and i.lower() == i:
        count += 1
    elif i.lower() in myDict and i not in myDict[i.lower()]:
        count += 1
    
print(count)