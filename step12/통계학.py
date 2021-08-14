import sys
from collections import Counter
N = int(sys.stdin.readline())
NumList=[]
for _ in range(N):
    NumList.append(int(sys.stdin.readline()))
NumList.sort()

counter = Counter(list(map(str,NumList)))
order = counter.most_common()
maxium = order[0][1]
max_num=[]
for x in order:
    if x[1] == maxium:
        max_num.append(x[0])
print(round(sum(NumList) / N))
print(NumList[(N+1)//2 - 1])
if len(max_num) > 1:
    print(max_num[1])
else:
    print(max_num[0])
print(max(NumList) - min(NumList))