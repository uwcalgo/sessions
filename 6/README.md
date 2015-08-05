# Session 6

###### 5 August 2015


Programming Methods
===================

## [Dynamic Programming](https://www.codechef.com/wiki/tutorial-dynamic-programming)

"Dynamic programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems. It is applicable to problems exhibiting the properties of overlapping subproblems and optimal substructure. When applicable, the method takes far less time than other methods that don't take advantage of the subproblem overlap." [Reference](https://en.wikipedia.org/wiki/Dynamic_programming)

#### Minimum steps to 1

```python
'''
On a positive integer, you can perform any one of the following 3 steps.

1.) Subtract 1 from it. ( n = n - 1 )
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  )

Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1.
'''

#---------------------------------------------------------------------------------------------#

'''
SOLUTION:

It all starts with recursion :).

F(n) = 1 + min(F(n-1), F(n/2), F(n/3)) if n > 1 else 0(i.e., F(1)=0)

Now that we have our recurrence equation, we can right way start coding the recursion.
Wait.., does it have over-lapping subproblems? YES.
Is the optimal solution to a given input depends on the optimal solution of its subproblems? Yes.
Bingo! its DP :)

So, we just store the solutions to the subproblems we solve and use them later on,
as in memoization or we start from bottom and move up till the given n, as in dp.
'''

from functools import lru_cache

# memoization solution (top down approach)
@lru_cache()
def memoi_sol(m):
    #global memo
    if m == 1:
        return 0

    #we have solved it already
    #if memo[m] != -1:
    #    return memo[m]

    # 3 cases
    result = 1 + memoi_sol(m-1) # case 1

    if m%2 == 0:
        result = min(result, 1 + memoi_sol(int(m/2))) # case 2

    if m%3 == 0:
        result = min(result,1 + memoi_sol(int(m/3))) # case 3

    #memo[m] = result # remember result

    return result

# bottom-up (DP)
def dp_sol(m):
    dp = [0]*(m+1)
    for i in range(2,m+1):
        # 3 cases
        dp[i] = 1 + dp[i-1] # case 1

        if i%2 == 0: # case 2
            dp[i] = min(dp[i], 1 + dp[int(i/2)])

        if i%3 == 0: # case 3
            dp[i] = min(dp[i], 1 + dp[int(i/3)])

    return dp[m]


from sys import argv
if __name__ == '__main__':
    k = int(argv[1])
    #memo = [-1]*(k+1)

    print ("memoization solution: %d"%memoi_sol(k))
    print ("dp solution: %d"%dp_sol(k))

```

## Python 3

### lru_cache

"Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable." [Reference](https://docs.python.org/3/library/functools.html#functools.lru_cache)

```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

### Decorators

```python
>>> def outer(some_func):
...     def inner():
...         print "before some_func"
...         ret = some_func() # 1
...         return ret + 1
...     return inner
>>> def foo():
...     return 1
>>> decorated = outer(foo) # 2
>>> decorated()
before some_func
2
``` [Reference](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/#_9_decorators)
