import sys
T = int(sys.stdin.readline())
TestList=[]
for i in range(T):
    x= int(sys.stdin.readline())
    y=int(sys.stdin.readline())
    TestList.append([x,y])

def asfg(list):
    numlist = []
    first = list[0]
    final = list[1]
    for i in range(1,final+1):
        numlist.append(i)
    for x in range(first):
        for y in range(1,final):
            numlist[y]+=numlist[y-1]
    print(numlist[-1])

for a in TestList:
    asfg(a)