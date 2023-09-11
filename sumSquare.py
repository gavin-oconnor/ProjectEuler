# Problem 6

one2hundred = int(100*101/2)**2
sumSquares = 0
for i in range(1,101):
    sumSquares += i*i

print(one2hundred-sumSquares)

