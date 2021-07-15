import sys
C = int(sys.stdin.readline())
datalist =[]
for i in range(C):
    datalist.append(list(map(int, sys.stdin.readline().split())))

def printAvg(list):
    peopleNum = list[0]
    listAvg = (sum(list)-peopleNum)/peopleNum
    upAvnCnt=0
    for k in range(len(list) - 1):
        if list[k+1] > listAvg:
            upAvnCnt+=1
    upRate = round(upAvnCnt / peopleNum * 100,3)
    upRate1 = format(upRate,".3f")
    return upRate1

resultList = list(map(printAvg,datalist))

for k in range(len(resultList)):
    print(f'{resultList[k]}%')