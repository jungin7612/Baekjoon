import sys
n = int(sys.stdin.readline())
TestLIST=[]
for i in range(n):
    TestLIST.append(list(map(int,sys.stdin.readline().split())))
def adsf(list):
    x= list[0]
    y= list[1]
    gap= y - x
    i=0
    while 1:
        if (i * (i + 1) / 2 - 2*i  <= gap  and i * (i + 1)  >= gap):
            X = i
            break
        else:
            i += 1
    if i * (i + 1)>= gap and i * (i + 1) -i <gap:
        return 2*i
    else:
        return 2*i -1

for a in TestLIST:
    print(adsf(a))