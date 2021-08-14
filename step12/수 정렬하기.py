import sys

N = int(sys.stdin.readline())
NumList = []
for _ in range(N): #버블 정렬
    NumList.append(int(sys.stdin.readline()))
for x in range(len(NumList)):
    for y in range(len(NumList) - x - 1):
        if NumList[y] > NumList[y + 1]:
            NumList[y], NumList[y + 1] = NumList[y + 1], NumList[y]

for a in NumList:
    print(a)
