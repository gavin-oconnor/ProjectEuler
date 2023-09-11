# Problem 3
import math

def prime_factorize(a):
    factors = []
    while a % 2 == 0:
        factors.append(2)
        a = a/2
    for i in range(3,int(math.sqrt(a)+1)):
        while(a % i == 0):
            factors.append(i)
            a = a/i
    if(a > 2):
        factors.append(a)
    return factors

# print(max(prime_factorize(600851475143)))
