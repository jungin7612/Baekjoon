import sys
N = int(sys.stdin.readline())
data= sys.stdin.readline().rstrip()
newdata = data.replace("J","")
newdata1=newdata.replace("A","")
newdata2=newdata1.replace("V","")
if len(newdata2) == 0:
    print("nojava")
else:
    print(newdata2)

