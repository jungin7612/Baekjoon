import sys
number = int(sys.stdin.readline())
data=[]
for i in range(number):
    data.append(sys.stdin.readline().rstrip())

def scanO(list):
    cnt = 0;
    fin=0;
    for k in range(len(list)):
        if "O" == list[k]:
            cnt+=1
            fin += cnt
        else:
            cnt =0
    return fin

result2 = list(map(scanO,data))

for k in range(len(result2)):
    print(result2[k])
