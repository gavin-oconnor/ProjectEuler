# Problem 2

sum = 2

n1, n2 = 1,2
while n2 < 4*10**6:
    temp = n2
    n2 = n1 + n2
    n1 = temp
    if n2 % 2 == 0:
        sum += n2

print(sum)