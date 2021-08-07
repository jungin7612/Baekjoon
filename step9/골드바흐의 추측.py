import sys
import math

T = int(sys.stdin.readline())
NumList=[]
for x in range(T):
    NumList.append(int(sys.stdin.readline()))

def getPrimeNum(n):
    sieve =[True] * (n+1)
    m = int(math.sqrt(n))
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    prime =  [i for i in range(2,n+1) if sieve[i] == True]
    plusPrime=[]
    for a in prime:
        for x in prime:
            if a+x == n:
                plusPrime.append([a,x])
    minnum=100000000000
    for b in plusPrime:
        if max(b)-min(b) <=minnum:
            minPrime=b
            minnum=max(b)-min(b)
    return sorted(minPrime)

for x in NumList:
    for a in getPrimeNum(x):
        print(a,end=" ")
    print("")

