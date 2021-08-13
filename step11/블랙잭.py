import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().split())
NumList = list(map(int,sys.stdin.readline().split()))
comList = list(combinations(NumList,3))
Max =0

for i in comList:
    tmp = sum(i)
    if Max <= tmp <=M:
        Max =tmp
print(Max)


