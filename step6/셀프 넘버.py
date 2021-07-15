def divide(num):
    numlist=[]
    num2 = str(num)
    for i in range(len(str(num))):
        numlist.append(num2[i])
    return numlist

def createNumber(num):
    numList = divide(num)
    SumeachNum =0
    for k in range(len(numList)):
        SumeachNum += int(numList[k])
    num1 = num + SumeachNum
    return num1

list1 =[]

for i in range(10000):
    list1.append(createNumber(i))
set1=set(list1)

for l in range(10000):
    if l not in set1:
        print(l)


