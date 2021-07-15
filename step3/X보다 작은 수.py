import sys
numList=[];
numCount,x = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
for k in range(len(num)):
    if num[k] < x:
        numList.append(num[k])
for a in numList:
    print(a,end=' ')