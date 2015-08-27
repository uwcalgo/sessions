# Session 7

###### 26 August 2015

Sieve of Eratosthenes
=====================
###### Finding primes

```python
def sieve(n):
    not_prime = []
    prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return prime
  ```

  Adapted from [iamrafiul](https://iamrafiul.wordpress.com/2013/04/28/sieve-of-eratosthenes-in-python/)

  ```python
  def sieve(n):
        n -= 1
        a = [True]*n
        ret = []

        for i in range(2,n+2):
                if(not a[i-2]):
                        continue
                for j in range(i*i,n+2,i):
                        a[j-2] = False

        for i in range(n):
                if(a[i]):
                        ret.append(i+2)

        return ret
  ```

  My implementation.

  ```python
  def smallPrimes(n):
    """Given an integer n, compute a list of the primes < n"""

    if n <= 2:
        return []

    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3)//2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom-top)//si)

    return [2]+filter(None, sieve)
  ```

  Adapted from [x]() by [HristoZA](https://github.com/HristoZA)

  Problem
  =======

  Sum of prime from the Standard Bank IT challenge 2015 final problems.

  Given a number X, give the number of unique sum of two primes which gives X.

  Example, X=16
  11 + 5 = 16
  13 + 3 = 16

  2 unique sums

  This problem is rated easy.
