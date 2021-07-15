yearnum = int(input())
if yearnum % 4 == 0 and (yearnum % 100 !=0 or yearnum % 400 == 0):
    print(1)
else:
    print(0)