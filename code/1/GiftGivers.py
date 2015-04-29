
# some sample data for the problem
# from http://uva.onlinejudge.org/external/1/119.html

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


# real program starts here
# StringIO allows us to treat strings as file-like objects
# see: https://docs.python.org/2/library/stringio.html

from StringIO import StringIO

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
            amount_given = int(fields[1])
            num_given_to = int(fields[2])
            people_given_to = fields[3:]
            amounts[name] = amounts.get(name, 0) - amount_given
            if num_given_to > 0:
                for person in people_given_to:
                    amounts[person] = (amounts.get(person, 0) 
                                       + (amount_given/num_given_to))
        result = ""
        for name in people:
            result += "{} {}\n".format(name, amounts[name])
        return result
    
result = process_givers(input_file)
while result:
    print result
    result = process_givers(input_file)
