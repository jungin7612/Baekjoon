import sys
N =int(sys.stdin.readline())
for _ in range(N):
    N1, N2 = map(int, sys.stdin.readline().split())
    a, b = N1, N2
    while N1 != 0 and N2 != 0:
        if N1 > N2:
            N1 = N1 % N2
        else:
            N2 = N2 % N1
    print(a * b // (N1 + N2))

