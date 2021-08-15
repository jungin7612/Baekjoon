import sys
N = int(sys.stdin.readline())
dataList=[]
for _ in range(N):
    dataList.append(sys.stdin.readline().split())
for x in dataList:
    for i in x:
        print(i[::-1],end=" ")
    print("")
