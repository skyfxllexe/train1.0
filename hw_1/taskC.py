num1 = input()
num2 = input()
num3 = input()
num4 = input()
nums = [num2,num3,num4]
def numEdit(num: str) -> str:
    temp = num.replace('-', '')
    temp = temp.replace('(','')
    temp = temp.replace(')','')
    temp = temp.replace('+', '')
    if len(temp) == 11:
        return temp[1:4] + temp[4:]
    elif len(temp) == 7:
        return '495' + temp 

for i in nums:
    if numEdit(num1) == numEdit(i):
        print('YES')
    else:
        print('NO')

