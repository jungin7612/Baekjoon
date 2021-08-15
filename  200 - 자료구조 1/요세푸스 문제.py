import sys
from _collections import deque
N,K = map(int,sys.stdin.readline().split())
dq = deque([i for i in range(1,N+1)])
NList=[]

while len(dq) > 0:
    for _ in range(K):
        x = dq.popleft()
        dq.append(x)
    NList.append(dq.pop())

NList=list(map(str,NList))
print("<"+", ".join(NList)+">")
# 나중에 rotate 로 다시 풀어보자

