import sys
NumList= list(map(int,sys.stdin.readline().split()))
if sorted(NumList) == NumList:
    print("ascending")
elif sorted(NumList,reverse=True) == NumList:
    print("descending")
else:
    print("mixed")

