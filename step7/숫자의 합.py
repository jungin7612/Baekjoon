import sys
N = int(sys.stdin.readline())
number = sys.stdin.readline().rstrip()
numlist=[]
for i in range(len(number)):
    numlist.append(number[i])
print(sum(list(map(int,numlist))))