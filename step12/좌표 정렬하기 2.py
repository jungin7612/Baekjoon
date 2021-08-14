import sys
N = int(sys.stdin.readline())
NumList =[]
for _ in range(N):
    tmpList = list(map(int,sys.stdin.readline().split()))
    tmpList.reverse()
    NumList.append(tmpList)
NumList.sort()
for x in NumList:
    print(x[1],x[0])