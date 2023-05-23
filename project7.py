#find the nth prime number
# I am using sieve of eratosthenes

primes = list()

def sieve():
    n = 1000000 
    p = 2
    prime = list([True for i in range(n+1)])

    while p**2 <= n+1:
        if prime[p] == True:
            for i in range(p**2,n+1,p):
                prime[i] = False
        p += 1
    

    for j in range(2,n+1):
        if prime[j]:
            primes.append(j)

sieve()

print(primes[10000])
