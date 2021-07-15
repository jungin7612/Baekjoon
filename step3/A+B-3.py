key = int(input())
num1,num2=0,0;
for i in range(key):
    num1,num2 = input().split()
    numa,numb = int(num1),int(num2)
    print(numa+numb)