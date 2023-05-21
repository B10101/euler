from functools import reduce

def multiples(n,m):
    return n*m

lis = list()
for i in range(100,1000):
    for j in range(100,1000):
        result = multiples(i,j)
        if str(result) == str(result)[::-1]:
            lis.append(result)

rel = reduce(max,lis)
print(rel)


