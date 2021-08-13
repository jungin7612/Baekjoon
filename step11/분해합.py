import sys
N = int(sys.stdin.readline())
min = 1000000000000
for i in range(N):
    nList = map(int, str(i))
    if N - i - sum(nList) == 0:
        tmp = i
        if tmp <= min:
            min = tmp
if min == 1000000000000:
    print(0)
else:
    print(min)