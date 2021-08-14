import sys # 다시 볼 필요가 있음 !
N,M = map(int, sys.stdin.readline().split())
CheckList=[]
mini=[]
for _ in range(N):
    CheckList.append(sys.stdin.readline().rstrip())

for i in range(N - 7):
    for x in range(M - 7):
        min1 = 0
        min2=0
        for k in range(i,i+8):
            for y in range(x,x+8):
                if (k+y) % 2 ==0:
                    if CheckList[k][y] != 'W':
                        min1+=1
                    if CheckList[k][y] != 'B':
                        min2+=1
                else:
                    if CheckList[k][y] != 'B':
                        min1 += 1
                    if CheckList[k][y] != 'W':
                        min2 += 1
        mini.append(min1)
        mini.append(min2)

print(min(mini))
