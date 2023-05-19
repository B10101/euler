#Finding the largest prime factor
from functools import reduce
import math
#finding the factors of the given number
def factors(n):    
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#finding out if they are prime
y =list()
def is_prime(h):
    max_div = math.floor(math.sqrt(h))
    for i in range(3, 1 + max_div, 2):
        if h % i == 0:
            return False
    return True

#combining the two and getting the maximum value
z = list()
for j in factors(600851475143):
    if is_prime(j):
        z.append(j)

rel = reduce(max,z)
print(rel)

