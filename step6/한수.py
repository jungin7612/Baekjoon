import sys
N = int(sys.stdin.readline())

def divideNum(number):
    num = str(number)
    numlist = []
    for i in range(len(num)):
        numlist.append(num[i])
    numlist1=list(map(int,numlist))
    return numlist1

def checkSequence(list):
    if len(list) == 1:
        return True
    elif len(list) == 2:
        return True
    elif len(list) == 3:
        if list[1] * 2 == list[0]+list[2]:
            return True
        else:
            return False
    elif len(list) == 4:
        if list[1] * 2== list[0]+list[2] and list[2] *2 == list[1]+list[3]:
            return True
        else:
            False

cnt=0
for k in range(N):
    if checkSequence(divideNum(k+1)) == True:
        cnt+=1
    else:
        pass
print(cnt)