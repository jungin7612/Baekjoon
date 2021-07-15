import sys
num = sys.stdin.readline().rstrip()

def inspectNum(number):
    if int(number)>= 10:
        number1 = number
        return number1
    elif int(number) <10:
        number1 = number+"0"
        return number1

cnt=0
num=inspectNum(num)
tmp= num

while True:
    if int(num[0])+int(num[1]) >= 10:
        num = num[1] + str(int(num[0]) + int(num[1]))[1]
        cnt += 1
        if num == tmp:
            break
    elif int(num[0])+int(num[1]) < 10:
        num = num[1] + str(int(num[0]) + int(num[1]))
        cnt += 1
        if num == tmp:
            break
print(cnt)

# 정석
input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정
print(cnt)