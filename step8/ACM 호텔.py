import sys

n = int(sys.stdin.readline())
TestLIST=[]
for i in range(n):
    TestLIST.append(list(map(int,sys.stdin.readline().split())))

def printResult(list):
    H = list[0]
    N = list[2]
    if N % H==0:
        first = H
        final = N // H
    else:
        first = N % H
        final = N // H + 1
    if final >= 10:
        asdf = int("{}{}".format(first, final))
    else:
        asdf = int("{}0{}".format(first, final))
    return asdf

for a in TestLIST:
    print(printResult(a))

