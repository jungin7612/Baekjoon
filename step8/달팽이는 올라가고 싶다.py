import sys
import math
NList = list(map(int,sys.stdin.readline().split()))
A = NList[0]
B = NList[1]
V = NList[2]
X = V - A
DF= A - B
print(math.ceil(X / DF) + 1)

