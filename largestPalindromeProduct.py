# Problem 4
import math

mx = 0

for x in range(999,99,-1):
    for y in range(999,99,-1):
        product = str(x*y)
        if product == product[::-1]:
            mx = max(mx,x*y)

print(mx)