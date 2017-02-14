def primecheck(n):
    if n == 2: return True
    if n == 0 or n == 1 or n%2==0: return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve(n):
    """Return a list of the primes below n."""
    prime = [True] * n
    for p in range(3, int(n**0.5)+1, 2):
        if prime[p]:
            for i in range(p * p, n, 2 * p):
                prime[i] = False
    return [2] + [p for p in range(3, n, 2) if prime[p]]
