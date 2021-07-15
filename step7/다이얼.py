import sys
word = sys.stdin.readline().rstrip()

def alpha(x):
    tmp=0
    if ord(x) >= 80 and ord(x) < 84:
        return 7
    elif ord(x) >= 84 and ord(x) < 87:
        return 8
    elif ord(x) >= 87 and ord(x) < 91:
        return 9
    else:
        for i in range(0,15,3):
            if (ord(x)-2) / 3 >= 21+(i/3):
                tmp = round((i/3)+2)
        return tmp

sum=0
for i in range(len(word)):
    sum+=alpha(word[i])+1
print(sum)
