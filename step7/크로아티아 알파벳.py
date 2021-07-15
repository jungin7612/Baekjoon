import sys
word = sys.stdin.readline().rstrip()
data =['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(len(data)):
    if data[i] in word:
        word= word.replace(data[i],"a")
    else:
        pass
print(len(word))
# for k in range(len(wordlist)):
#     word = word.replace(wordlist[k],"")
#     cnt+=1
#
# sum = len(word)
# print(cnt+sum)
