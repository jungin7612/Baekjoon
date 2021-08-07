import sys
N = int(sys.stdin.readline())
if N == 1:
    pass
else:
    for x in range(2,N+1):
        if N % x == 0:
            while N % x ==0:
                N =N // x
                print(x)