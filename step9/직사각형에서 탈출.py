import sys
x,y,w,h = map(int,sys.stdin.readline().split())

halfW = w / 2
halfH = h /2
minDistance=[]
if x >= halfW:
     minDistance.append(w - x)
elif x < halfW:
    minDistance.append(x)
if y >= halfH:
    minDistance.append(h -y)
elif y < halfH:
    minDistance.append(y)
print(min(minDistance))
