import sys
N = int(sys.stdin.readline())
numList=[]
for i in range(N):
    numList.append(sys.stdin.readline().rstrip())


def checkGroupWord(word):
    tmp=word[0]
    tmpList=[tmp,]
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i + 1] not in tmpList:
                tmpList.append(word[i+1])
            else:
                return 0
        else:
            pass
    return 1
numList1 = list(map(checkGroupWord,numList))
print(numList1.count(1))