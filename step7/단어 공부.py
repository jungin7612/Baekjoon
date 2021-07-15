import sys
word = sys.stdin.readline().rstrip()
lowerword = word.lower()
setword = list(set(lowerword))
max = 0
x = ''
for i in range(len(setword)):
    cnt = lowerword.count(setword[i])
    if max < cnt:
        max =cnt
        x=setword[i]
    elif max == cnt:
        x ='?'
print(x.upper())

