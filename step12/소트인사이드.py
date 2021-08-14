import sys
Num = sys.stdin.readline().rstrip()
NumList = list(map(int,Num))
NumList.sort(reverse=True)
for num in NumList:
    print(num, end="")