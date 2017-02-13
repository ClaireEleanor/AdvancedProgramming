def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def primecheck(n):
    if n == 2: return True
    if n == 0 or n == 1 or n%2==0: return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
