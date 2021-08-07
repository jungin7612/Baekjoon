import sys
XList=[]
YList=[]
for i in range(3):
    x,y = map(int,sys.stdin.readline().split())
    XList.append(x)
    YList.append(y)
for x in XList:
    if XList.count(x) == 1:
            Xanswer= x
for y in YList:
    if YList.count(y) == 1:
            Yanswer= y
print(Xanswer,Yanswer)