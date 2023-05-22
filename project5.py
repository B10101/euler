#finding th least number evenly divisible by numbers 1 through 20
#Using gcd from fractions, lcm = a*b/gcd

from math import lcm
from functools import reduce

print(reduce(lambda a,b : lcm(a,b), range(1,21)))
