import sys

N = int(sys.stdin.readline())
n=1
if N ==1:
    print(1)
else:
    while N > 1:
        N = N - (6 * n)
        n += 1
    print(n)