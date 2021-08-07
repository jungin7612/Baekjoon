import sys
M=int(sys.stdin.readline())
N=int(sys.stdin.readline())
NumList=[]
for a in range(M,N+1):
    status = True
    if a == 1:
        status=False
    for x in range(2, a):
        if a % x == 0:
            status = False
            break
    if status == True:
        NumList.append(a)
    else:
        pass
if not NumList:
    print(-1)
else:
    print(sum(NumList))
    print(min(NumList))