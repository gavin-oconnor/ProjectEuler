# Problem 1

sum = 0

for num in range(1000):
    if num % 3 == 0:
        sum += num
    elif num % 5 == 0:
        sum += num

print(sum)