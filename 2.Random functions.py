# Random Functions
l1 = [1,2,3,4,5,6]

import random as rd


a =rd.choice([1,2,3,4,5,6])
a

# Generate random flot number between 0<=random<1
b=rd.random()  
b

# genearte radon interger for given range (doesnt work for float values)
#it include last item and no step but in randrange not include last item and have step.
c=rd.randint(2,6)  
c

# generate a random interger number in given range 
d=rd.randrange(10,103,5)  # 10,15,20,... 100
d

# generate a random interger number with given step
e=rd.randrange(10,100,5)
e

# Generate random floating number in given range 
f = rd.uniform(3,5)  
f

l1 = [1,2,3,4,5,6]

#Shuffle values in l1
rd.shuffle(l1)
l1

# seed means random number will be fixed for that particular seed value.
x1= rd.random()
x1

rd.seed(5)
x2= rd.random()
x2

rd.seed(7)
x3= rd.random()
x3

rd.seed(1)
x4= rd.random()
x4

rd.seed(5)
x9= rd.random()
x9

rd.seed(3)
x6= rd.random()
x6

rd.seed(7)
x7= rd.random()
x7

