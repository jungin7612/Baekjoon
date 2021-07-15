import sys
num = int(sys.stdin.readline())
star= "*"
for i in range(num+1):
    if i >=1:
        print((star*i).rjust(num))