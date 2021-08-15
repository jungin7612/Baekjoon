import sys
from collections import deque

stack = deque()

N = int(sys.stdin.readline())
for _ in range(N):
    tmpList = sys.stdin.readline().split()
    if tmpList[0] == "push":
        stack.append(tmpList[1])
    elif tmpList[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif tmpList[0] == "size":
        print(len(stack))
    elif tmpList[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif tmpList[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)