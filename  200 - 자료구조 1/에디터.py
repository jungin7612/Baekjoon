import sys

letter = list(sys.stdin.readline().strip())
tmp = []
M = int(sys.stdin.readline())

for _ in range(M):
    tmpList = sys.stdin.readline().split()
    if tmpList[0] == 'P':
        letter.append(tmpList[1])
    elif tmpList[0] == 'L' and letter != []:
        tmp.append(letter.pop())
    elif tmpList[0] == 'D' and tmp != []:
        letter.append(tmp.pop())
    elif tmpList[0] == 'B' and letter != []:
        letter.pop()

print("".join(letter + list(reversed(tmp))))
