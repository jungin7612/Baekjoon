import sys
T = int(sys.stdin.readline())
datalist=[]

def iterable(x):
    n = int(x[0])
    data =x[1]
    for i in range(len(data)):
        for k in range(n):
            print(data[i],end="")
    return 0


for i in range(T):
    datalist.append(sys.stdin.readline().split())

for i in range(len(datalist)):
    iterable(datalist[i])
    print("")
