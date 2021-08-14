import sys
N = int(sys.stdin.readline())
NumList =[]
for _ in range(N):
    NumList.append(list(map(int,sys.stdin.readline().split())))
NumList.sort()
for x in NumList:
    print(x[0],x[1])