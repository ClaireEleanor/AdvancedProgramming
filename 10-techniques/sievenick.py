
def sieve(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
        # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
