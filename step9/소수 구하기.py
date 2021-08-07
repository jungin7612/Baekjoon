import sys
import math

M,N = map(int,sys.stdin.readline().split())

def getPrimeNum(n):
    sieve =[True] * (n+1)
    m = int(math.sqrt(n))
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    return [i for i in range(2,n+1) if sieve[i] == True]

for a in getPrimeNum(N):
    if a >= M:
        print(a)
    else:
        pass



