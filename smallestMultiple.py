# Problem 5
import math

# 20 --> 10,5,4,2
# 19 --> 19
# 18 --> 9,6,3
# 17 --> 17
# 16 --> 16,4
# 15 --> 5,3
# 14 --> 7,2
# 13 --> 13
# 12 --> 4,3
# 11 --> 11

initialNum = 20*19*18*17*16*14*13*12*11
def brute_force():
    for i in range(2,initialNum,2):
        ret = True
        if i % 10**6 == 0:
            print(i)
        for j in [11,19,13,17,16,14,18,12,20]:
            if i % j != 0:
                ret = False
        if ret:
            return i
        
def prime_factorize(a):
    factors = {}
    while a % 2 == 0:
        factors[2] = factors.get(2,0) + 1
        a = int(a/2)
    for i in range(3,int(math.sqrt(a)+1)):
        while(a % i == 0):
            factors[i] = factors.get(i,0) + 1
            a = int(a/i)
    if(a > 2):
        factors[a] = factors.get(a,0) + 1
    return factors
        
def prime_factors():
    prime_factors = [prime_factorize(i) for i in range(2,21)]
    counts = {}
    for d in prime_factors:
        for k,v in d.items():
            counts[k] = max(counts.get(k,0),v)
    product = 1
    for k,v in counts.items():
        product *= k**v
    return product
        
print(prime_factors())
