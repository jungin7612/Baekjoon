import sys
numList = list(sys.stdin.readline().split())
num1= numList[0][::-1]
num2 = numList[1][::-1]
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)