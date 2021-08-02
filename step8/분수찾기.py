import sys

N = int(sys.stdin.readline())
i=1

while 1:
    if(i * (i+1)/2 -i-1 <= N and i * (i+1) / 2 >= N):
        X = i
        break
    else:
        i+=1
count = int(N - ((X-1)* X / 2))

if X % 2 == 0:
    qnstn = "{}/{}".format(count, X + 1 - count)
else:
    qnstn = "{}/{}".format(X + 1 - count,count)

print(qnstn)