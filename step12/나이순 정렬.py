import sys
N = int(sys.stdin.readline())
PList=[]
for i in range(N):
    tmpList = sys.stdin.readline().split()
    tmpList[0] = int(tmpList[0])
    tmpList.insert(1,i)
    PList.append(tmpList)
PList.sort()
for x in PList:
    print(x[0],x[2])