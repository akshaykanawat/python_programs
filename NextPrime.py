#next prime number

factors= lambda n:[x for x in range(1,n+1) if (n%x)==0]
is_prime= lambda n: len(factors(n))==2

def NextPrime(n):
    nxt=n+1
    if is_prime(n)==True:
        while not is_prime(nxt):
            nxt+=1
        return nxt