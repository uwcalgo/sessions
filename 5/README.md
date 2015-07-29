# Session 5 

###### 29 July 2015

		
Problems
========

###	[Crowd Control](http://www.olympiad.org.za/olympiad/wp-content/uploads/2014/09/2014-SBITC-Complete-problem-set.pdf) (H)

Rated hard, this is problem 2 from the [SBITC 2014 problem set](http://www.olympiad.org.za/olympiad/wp-content/uploads/2014/09/2014-SBITC-Complete-problem-set.pdf).

### Collaboration in session

I made a mistake with the second test case where I made the stage height 4m instead of 2m.
Here is what it looks like with 2m.

![Crowd control test 2](http://i.imgur.com/pd41fOJ.png)

This can be generated with the following python code:

```python
import matplotlib.pyplot as plt

plt.plot([1,1.2,1.4,2,2.2], [2.9,3.2,3.3,4.5,4.4], 'ro')
plt.plot([0,1], [2,2.9])
plt.plot([0,1.2], [2,3.2])
plt.plot([0,1.4], [2,3.3])
plt.plot([0,2], [2,4.5])
plt.plot([0, 2.2], [2,4.4])


plt.axis([0, 0.5, 0, 5])

plt.ylabel('Stage height in meters')
plt.xlabel('Distance from stage in meters')
plt.show()
```
