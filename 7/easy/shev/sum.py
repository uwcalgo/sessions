#!/usr/bin/python

def sieve(n):
        n -= 1
        a = [True]*n

        for i in range(2,n+2):
                if(not a[i-2]):
                        continue
                for j in range(i*i,n+2,i):
                        a[j-2] = False

        ret = []

        for i in range(n):
                if(a[i]):
                        ret.append(i+2)

        return ret

def sumP(primes, n):
        counter = 0

        for x in range(0,len(primes)/2):
                if(n-primes[x] in primes):
                        counter += 1

        return counter

n = input()
print(sumP(sieve(n), n))
