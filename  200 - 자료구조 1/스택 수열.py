import sys
from _collections import deque

n = int(sys.stdin.readline())
NList = []
dq = deque()
result = []
for _ in range(n):
    NList.append(int(sys.stdin.readline()))
i = 0
x = 1
tmpList = []
while True:
    try:
        if NList[i] >= x:
            dq.append(x)
            tmpList.append("+")
            x += 1
        elif NList[i] < x:
            result.append(dq.pop())
            tmpList.append("-")
            i += 1
    except:
        break

if result == NList:
    for x in tmpList:
        print(x)
else:
    print("NO")
