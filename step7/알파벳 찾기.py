import sys
char = sys.stdin.readline().rstrip()

for i in range(26):
    print(char.find(chr((97+i))),end=" ")


