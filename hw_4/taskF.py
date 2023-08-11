import sys
s = sys.stdin.read()

s = s.split('\n')
s = s[:len(s)-1]

db = dict()
key = dict()
for i in s:
    temp = i.split(' ')
    key[temp[1]] = int(temp[2])
    if temp[0] in db.keys() and temp[1] in db[temp[0]].keys():
        db[temp[0]][temp[1]] += int(temp[2])
    elif temp[0] in db.keys() and temp[1] not in db[temp[0]].keys():
        db[temp[0]][temp[1]] = int(temp[2])
    if temp[0] not in db.keys():
        db[temp[0]] = key
    key = dict()

for i in sorted(db.keys()):
    print(i + ':')
    for j in sorted(db[i]):
        print(j, db[i][j])