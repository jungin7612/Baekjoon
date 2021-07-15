num1,num2 = input().split()
hour,min = int(num1),int(num2)

if min - 45 < 0:
    if hour -1 < 0:
        hour = 23
        min = 60 + (min - 45)
    else:
        hour=hour -1
        min = 60 + (min- 45)
elif min - 45 >= 0:
    min = min - 45

print(hour,min)
