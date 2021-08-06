import sys
N = int(sys.stdin.readline())
variable = N
three=0
while variable > 0:
    if variable % 3 != 0 and variable % 5 !=0:
        variable -= 5
    elif variable % 3 == 0 and variable % 5 !=0:
        three = variable
        variable -= 5
    elif variable % 5==0:
        break
five = N - three
if five % 5 != 0 or three % 3 !=0:
    print(-1)
else:
    print(five // 5 + three // 3)