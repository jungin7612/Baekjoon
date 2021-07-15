import sys
N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
Max = max(data)

newdata = list(map(lambda x: x/Max *100,data))
avg = sum(newdata) / len(newdata)
print(avg)