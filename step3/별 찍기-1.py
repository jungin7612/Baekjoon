import sys
num = int(sys.stdin.readline())
for i in range(num):
    if i >= 1:
        print('')
    for k in range(i+1):
        print("*",end='')