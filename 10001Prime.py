# Problem 7
import math

def check_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(num)+1),2):
        if num % i == 0:
            return False
    return True

def which_prime(which):
    nums = [2,3]
    possible = 5
    while len(nums) < which:
        if check_prime(possible):
            nums.append(possible)
        possible += 2

    return nums[-1]

print(which_prime(10001))