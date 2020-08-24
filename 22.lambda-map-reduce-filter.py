# lambda Function - Anonymous function - Inline function
# function without a name and create function with lambda keyword.
#This function can have any number of arguments but only one expression,which is evaluated and returned.

# normal function and Lanbda function

def cube(n):
    return n*n*n

def gt(x):
    if x>10:
        return 10
    

g=lambda n: n*n*n

# calling of functions.

print(cube(3))
print(g(3))
# Another lambda example

tot= lambda x,y,z: x+y+z
print(tot(4,5,6))


# Map - function will execute for each entry in the sequence
# syntax- map(func, seq)

l1=[2,3,4,5]
res=map(cube,l1)
result = tuple(map(cube,l1))  # can convert into list aswell 
print(result) 

l1=[2,3,4,5]
result = tuple(map(lambda x: x*x*x ,l1))  # can convert into list aswell 
print(result) 


# Filter 
# result = filter(func,seq)

# lambda function calling in filter 
# check condition for each entry in sequence if true retunr value else nothing.
#syntax- filter(func, seq)

l2 = [i for i in range(1,101)] 
l2

res=filter(lambda t = t%2==0, l2)
res

final_list = list(filter(gt, l2))  # if condition pass then retun some value so its consider as true else no value.
print(final_list) 


final_list = list(filter(lambda x: (x%2 != 0) , l2)) 
print(final_list) 


# reduce - for accumulation sum etc..
#syntax- reduce(func, seq)

from functools import reduce

l3 = [i for i in range(1,10)]
l3

final_sum=reduce(lambda x,y:x+y,l3) 
print(final_sum)