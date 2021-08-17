import sys
N = int(sys.stdin.readline())
if N == 0:
    print(0)
    exit()
result = N
while N > 1:
    N-=1
    result *= N
a = str(result)[::-1]
cnt=0
for x in a:
    if x != '0':
        break
    else:
        cnt+=1
print(cnt)


