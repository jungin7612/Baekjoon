import sys
N = int(sys.stdin.readline())
NumList= list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MList =list(map(int,sys.stdin.readline().split()))

for x in MList:
    if x in NumList:
        print(1)
    else:
        print(0)