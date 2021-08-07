import sys

T = int(sys.stdin.readline())
NumList = []
for x in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        NumList.append(-1)
    else:
        rp = r1 + r2
        rm = max([r1, r2]) - min([r1, r2])
        if rp > distance > rm:
            NumList.append(2)
        elif distance == rm or distance == rp:
            NumList.append(1)
        elif rp < distance or rm > distance or distance==0:
            NumList.append(0)

for x in NumList:
    print(x)
