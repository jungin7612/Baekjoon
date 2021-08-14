import sys

N = int(sys.stdin.readline())
NumList = list(map(int, sys.stdin.readline().split()))
newList = sorted(set(NumList))
dic = {newList[i]: i for i in range(len(newList))}

for x in NumList:
    print(dic[x], end=" ")
