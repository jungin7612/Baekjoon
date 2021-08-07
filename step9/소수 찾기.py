import sys
N = int(sys.stdin.readline())
TestList= list(map(int,sys.stdin.readline().split()))
cnt=0

for a in TestList:
    status =True
    for x in range(2,a):
        if a % x == 0:
             status=False
             break
    if status==True:
        cnt+=1
    else:
        pass
if 1 in TestList:
    print(cnt -1)
else:
    print(cnt)