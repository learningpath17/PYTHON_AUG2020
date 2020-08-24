# 1. Shallow copy and deep copy
#shallow copy - create 2 copies with same memory
# Deep copy - create 2 separate copies with different memory spaces, 
import copy

#shallow copy
l1=[1, 2, [3,5], 4]
l1
l2=copy.copy(l1)
l1
l2
l2[2][0]=77
l1
l2

#deep copy
l1=[1, 2, [3,5], 4]
l1
l2=copy.deepcopy(l1)
l1
l2
l2[2][0]=77
l1
l2

#1. Polimorphism another type -duck typing.
class Circle:

    def corners(self):
        print("circle has no corners")
    
    def area(self):
        print("aread is pi(r**2) ")

class Rectangle:

    def corners(self):
        print("rectangle has 4 corners")
    
    def area(self):
        print("area is length*width ")

# common function to use class methods
def corners_area(shape):
        shape.corners()
        shape.area()

#instances / objects
cir = Circle()
rec = Rectangle()
# passing the object
corners_area(cir)
corners_area(rec)

#2.find the maximum occurance charatcter in the given string and it's position.  

st = 'abcdefghab'

len(st)

l=[]

for i in range (0,len(st)):
    cnt=0
    cnt= st.count(st[i])
    l.append(cnt)
l    

max(l)   
for i in range(0,len(l)):
    if l[i]==max(l):
        print(st[i])
        break

# 3. Monkey patching

class student:
        
    def stddt(self):
        print('Student details function in class..!' )

def monkey_stddt():
    print('Student details function in Monkey function..!' )
    
std=student()
std.stddt()

std.stddt = monkey_stddt

std.stddt()

# 4. Iterators  __iter__  and next (explicit iterators insted of automate by loops)

# An iterable user defined type 

class Test: 
  
    # Cosntructor 
    def __init__(self, limit): 
        self.limit = limit 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        self.x = 10
        return self
    
    # To move to next element, 
    def __next__(self): 
  
        # Store current value ofx 
        x = self.x 
  
        # Stop iteration if limit is reached 
        if x > self.limit: 
            raise StopIteration 
  
        # Else increment and return old value 
        self.x = x + 1; 
        return x 
  
# Prints numbers from 10 to 15 
for i in Test(15): 
    print(i) 
  
# Prints nothing 
for i in Test(5): 
    print(i)

# 5.Generators (Generator function bahave like iterators) - Yield key word.
#example -1
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(1, 5)
for i in generator:
    print(i)

#Example-2
def gameslist(): 
    yield 'Cricket'
    yield 'Volleyball'
    yield 'Football'
    yield 'Tennis'

# Driver code to check above generator function 
for value in gameslist():  
    print(value) 
    
# Example-3    
import time

def fib():
   a, b = 0, 1
   while True:
      yield b
      a, b = b, a + b

g = fib()

try:
   for e in g:
      print(e)
      time.sleep(1)

except KeyboardInterrupt:
   print("Calculation stopped")

#6. decorators

#Example-1   
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")
 
# Example-2
# defining a decorator 
def hello_decorator(func): 
  
    # inner1 is a Wrapper function in  
    # which the argument is called 
      
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
  
        # calling the actual function now 
        # inside the wrapper function. 
        func() 
  
        print("This is after function execution") 
          
    return inner1 
  
  
# defining a function, to be called inside wrapper 
def function_to_be_used(): 
    print("This is inside the function !!") 
  
# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 
  
  
# calling the function 
function_to_be_used() 

#Example-3  
# Decoration definaion
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

#def ordinary():
#    print("I am ordinary")

@make_pretty
def ordinary():
    print("I am ordinary")
    
#above satement is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
    
        
# sort on the second elements in the inside tuples.2,-6,3
l2=[(1,2),(5,-6),(4,3)]
l2.sort()
l2
l2.sort(reverse=True)
l2
l2.sort(key=lambda t: t[-1])
l2

# create a list with list identical list items as keys and their occurance as value. 
l=['a','b','a','c','b','a','d','d','c','b']


dict1={i:l.count(i) for i in l }
dict1

#prepare a dictionary with two different lists.
l1=[1,2,3,4,5]
l2=['a','b','c','d']
dict2=dict(zip(l1,l2))
dict2

