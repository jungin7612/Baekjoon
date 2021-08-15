import sys
N = int(sys.stdin.readline())
NList=sys.stdin.readline().split()
M = int(sys.stdin.readline())
MList = sys.stdin.readline().split()

N1 = eval('*'.join([str(n) for n in NList]))
M1 = eval('*'.join([str(n) for n in MList]))

while N1 != 0 and M1 != 0:
    if N1 > M1:
        N1 = N1 % M1
    else:
        M1 = M1 % N1
if len(str(N1+M1)) >= 9:
    print(str(N1+M1)[-9:])
else:
    print(N1+M1)