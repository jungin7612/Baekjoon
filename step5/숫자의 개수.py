import sys
data= []
for i in range(3):
    data.append(int(sys.stdin.readline()))
result = data[0] * data[1] * data[2]

proresult =list(str(result))
proresult2 = list(map(int,proresult))

for k in range(10):
    print(proresult2.count(k))

