import sys
K = int(sys.stdin.readline())
NumList=[]
for x in range(K):
    n = int(sys.stdin.readline())
    if n != 0:
        NumList.append(n)
    else:
        NumList.pop(-1)

print(sum(NumList))