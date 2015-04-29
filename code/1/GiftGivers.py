
# coding: utf-8

# In[18]:

data = """5
dave laura owen vick amr
dave 200 3 laura owen vick
owen 500 1 dave
amr 150 2 vick owen
laura 0 2 amr vick
vick 0 0
3
liz steve dave
liz 30 1 steve
steve 55 2 liz dave
dave 0 2 steve liz
"""


# In[3]:

from StringIO import StringIO


# In[19]:

input_file = StringIO(data)
def process_givers(input_file):
    try:
        num_people = int(input_file.next())
    except StopIteration:
        return False
    else:
        #print num_people
        people = input_file.next().rstrip().split()
        #print people
        amounts = dict()
        for num in range(num_people):
            line = input_file.next()
            fields = line.rstrip().split()
            name = fields[0]
            amount_given = float(fields[1])
            num_given_to = float(fields[2])
            people_given_to = fields[3:]
            amounts[name] = amounts.get(name, 0) - amount_given
            if num_given_to > 0:
                for person in people_given_to:
                    amounts[person] = (amounts.get(person, 0) 
                                       + (amount_given/num_given_to))
        return amounts
    
amounts = process_givers(input_file)
while amounts:
    print amounts
    amounts = process_givers(input_file)


# In[8]:

mylist = [1,2,3]
myslice = mylist[3:]
print myslice


# In[ ]:



