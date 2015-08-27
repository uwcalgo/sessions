# Session 4
###### 22 Jul 2015

Discussed languages
===================

## python

### functions

#### [zip](https://docs.python.org/2/library/functions.html#zip )

```
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True
```

#### [set](https://docs.python.org/2/library/functions.html#func-set )

```
>>> set([0, 1, 2, 3])
set([0, 1, 2, 3])
>>> set("obtuse")
set(['b', 'e', 'o', 's', 'u', 't'])
```

```
>>> s = set([12, 26, 54])
>>> s.add(32)
>>> s
set([32, 26, 12, 54])
```

reference: [wikibooks.org](https://en.wikibooks.org/wiki/Python_Programming/Sets)

#### [* **](https://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists )
```
>>> range(3, 6)             # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> range(*args)            # call with arguments unpacked from a list
[3, 4, 5]
```

```
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')

first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test
```

reference: [pythontips.com](http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)

Problems
========

### [Marching band](http://www.olympiad.org.za/olympiad/wp-content/uploads/2013/01/SBITC-Heats-Problems-v-13-04-14-Final.pdf) (M)

Rated medium, this is problem 3 from the [2013 Standard Bank IT Challenge heats](http://www.olympiad.org.za/olympiad/wp-content/uploads/2013/01/SBITC-Heats-Problems-v-13-04-14-Final.pdf).

###	[Crowd Control](http://www.olympiad.org.za/olympiad/wp-content/uploads/2014/09/2014-SBITC-Complete-problem-set.pdf) (H)

Rated hard, this is problem 2 from the [SBITC 2014 problem set](http://www.olympiad.org.za/olympiad/wp-content/uploads/2014/09/2014-SBITC-Complete-problem-set.pdf).
