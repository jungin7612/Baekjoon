import sys
from _collections import deque

N = int(sys.stdin.readline())
NList = []

for x in range(N):
    NList.append(sys.stdin.readline().rstrip())


def rotate(n):
    dq = deque()
    for x in n:
        if x == "(":
            dq.append(x)
        elif x == ")":
            try:
                dq.pop()
            except:
                dq.append(1)
                return dq
    return dq


for x in NList:
    if len(rotate(x)) == 0:
        print("YES")
    else:
        print("NO")
