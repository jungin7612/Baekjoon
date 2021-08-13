import sys
N = int(sys.stdin.readline())
dungList = []
for i in range(N):
    dungList.append(list(map(int,sys.stdin.readline().split())))

for x in dungList:
    cnt =1
    for y in dungList:
        if x[0] < y[0] and x[1] < y[1]:
            cnt+=1
    print(cnt, end=" ")