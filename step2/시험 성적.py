testNum= int(input())
alist = list(range(90,101))
blist = list(range(80,90))
clist = list(range(70,80))
dlist = list(range(60,70))

alllist=[alist,blist,clist,dlist]
strlist=["A","B","C","D","E"]
break1 = True
if testNum >= 60:
    for i in range(len(alllist)):
        for k in alllist[i]:
            if testNum == k:
                print(strlist[i])
else:
    print("F")

