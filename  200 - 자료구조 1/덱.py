from _collections import deque
import sys
queue = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    tmpList = sys.stdin.readline().split()
    if tmpList[0] == "push_back":
        queue.appendleft(tmpList[1])
    elif tmpList[0] == "push_front":
        queue.append(tmpList[1])
    elif tmpList[0] == "top":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    elif tmpList[0] == "size":
        print(len(queue))
    elif tmpList[0] == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif tmpList[0] == "pop_back":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif tmpList[0] == "pop_front":
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)
    elif tmpList[0] == "front":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    elif tmpList[0] == "back":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)