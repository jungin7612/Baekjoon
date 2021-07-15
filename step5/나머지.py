import sys
data=[]
for i in range(10):
    data.append(int(sys.stdin.readline()))

modulo = list(map(lambda x: x % 42, data))
moduloset = set(modulo)
print(len(moduloset))