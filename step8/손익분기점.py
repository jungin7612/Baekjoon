import sys
import math
data = list(map(int,sys.stdin.readline().split()))

const = data[0]
let = data[1]
fee = data[2]


if let >= fee:
    print(-1)
else:
    x = math.floor(-const / (let - fee) + 1)
    print(x)
