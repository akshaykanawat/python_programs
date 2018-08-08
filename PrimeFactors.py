def PrimeFactors(num):
    factors={}
    n=2
    
    while num!=1:
        while num % n== 0:
            num = num/n
            if n in factors:
                factors[n]+=1
            else:
                factors[n]=1
        n=n+1
    return factors
    
            
            

