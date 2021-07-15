import sys
data=list(map(int,sys.stdin.readline().split()))
dataset =[100,100,200,200,300,300,400,400,500]
check = ''
if sum(data) >= 100:
    for i in range(len(data)):
        if data[i] > dataset[i]:
            check="hacker"
            break
        else:
            check = "draw"
elif sum(data) < 100:
    for i in range(len(data)):
        if data[i] > dataset[i]:
            check = "hacker"
            break
        else:
            check = "none"
print(check)
