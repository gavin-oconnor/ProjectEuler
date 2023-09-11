# Problem 3
import math

def prime_factorize(a):
    while a % 2 == 0:
        print(2)
        a = a/2
    for i in range(3,int(math.sqrt(a)+1)):
        while(a % i == 0):
            print(i)
            a = a/i
    if(a > 2):
        print(a)

prime_factorize(600851475143)
