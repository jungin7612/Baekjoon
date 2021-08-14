import sys
N = int(sys.stdin.readline())
letterList=[]
for _ in range(N):
    letterList.append(sys.stdin.readline().rstrip())
letterList.sort()
letterList.sort(key=len)
result = []
for x in letterList:
    if x not in result:
        result.append(x)
        print(x)
