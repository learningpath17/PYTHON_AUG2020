# How to define a list- can define with any values - numeric,alpha and alpha numeric
l1=[2,4,6,1,88,44,5]
l2=['vij','abhi',55,'ram',7,3,99]
l3=['hyd','mum','che','ben']

# slicing on lists by using indexes whcih starts from 0 for forwad direction and
# for backward direction indexe starts from -1
l1[0]       # return first value in the list
l1[3:6]     # return the values from index 3 to index 5 (end index not include)
l1[-2]      # return value from last 2 nd as its backward reading
l1[2:]      # return all the values from index 2
l1[3] = 77  # to edit the index 3 value  

# functions on list 
lis1=[2,3,8,99,5,9]

len(lis1)
max(lis1)
min(lis1)

lis1.append(77) 
lis1

# exec and eval 

s= '4*5+6'
eval(s)
st='p=34'
exec(st)
st
p
# to know about function functionality.
# 

lis1.insert(2,66)
lis1

lis1.remove(99)
lis1

lis1.reverse()
lis1

lis2=lis1.sort()
lis2

lis2.sorted(lis1) 
lis2

lis1.sort()
lis1
lis1.sort(reverse=True)
lis1

lis1.count(2)  # return no of 2 are present in the list
lis1.index(2)  # return the index of value 2 

# two dimention lists
l2=[[1,2],[3,4],[5,6],[7,8]]
l2[2]
l2[1][0]


l1=[(1,2),(5,-6),(4,3)]
l1.insert(2,(5,5))
l1
l1.remove((5,5))
l1[0]
l1[0][1]
l1[1][0]=99

# sort on the second elements in the inside tuples.2,-6,3
l2=[(1,2),(5,-6),(4,3)]
l2.sort()
l2
l2.sort(reverse=True)
l2
l2.sort(key=lambda t: t[-1])

# Cancatination and repeatation for list
l1=[1,2,3]
l2=[4,5,6]
l1+l2
l1*3

# deletion of single element in list and total list deletion
del l1[1]
del l1