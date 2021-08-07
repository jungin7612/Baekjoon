import sys
Data=[]
while True:
    numList = list(map(int,sys.stdin.readline().split()))
    if sum(numList) ==0:
        break
    Data.append(numList)

def inspect(list):
    a= min(list)
    list.remove(a)
    c= max(list)
    list.remove(c)
    b = list[0]
    if a ** 2 + b ** 2 == c **2:
        print("right")
    else:
        print("wrong")

for x in Data:
    inspect(x)