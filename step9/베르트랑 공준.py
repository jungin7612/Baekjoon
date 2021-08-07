import sys
import math

NumList=[]
while True:
    N = int(sys.stdin.readline())
    if N != 0:
        NumList.append(N)
    else:
        break

def getPrimeNum(n):
    sieve =[True] * (2*n+1)
    m = int(math.sqrt(n*2))
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i,n*2+1,i):
                sieve[j] = False
    cnt=0
    for a in [i for i in range(2,n*2+1) if sieve[i] == True]:
        if a >n:
            cnt+=1
    return cnt

for x in NumList:
    print(getPrimeNum(x))