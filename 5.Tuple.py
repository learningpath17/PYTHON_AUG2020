# How to define a tuple - it can define with any values - numeric,alpha and alpha numeric
t1=(2,4,6,1,88,44,5)
t2=('vij','abhi',55,'ram',7,3,99)
t3=('hyd','mum','che','ben')

# slicing on tuple by using indexes whcih starts from 0 for forwad direction and
# for backward direction indexe starts from -1
t1[0]       # return first value in the list
t1[3:6]     # return the values from index 3 to index 5 (end index not include)
t1[-2]      # return value from last 2 nd as its backward reading
t1[2:]      # return all the values from index 2
t1[3] = 77  # to edit the index 3 value  

# functions on tuple  
tup1=(2,3,8,99,5,9)

len(tup1)
max(tup1)
min(tup1)

# As tuple is immutable can't perform any update functions like list below are not available for tuple
tup1.append(77) 
tup1.insert(2,66)
tup1.remove(99)
tup1.reverse()
tup1.sort()
tup1.sort(reverse=True)

# below are the available functions on tuple.
tup1.count(2)  # return no of 2 are present in the list
tup1.index(2)  # return the index of value 2 

# two dimention lists
t2=((1,2),(3,4),(5,6),(7,8))
t2[2]
t2[1][0]

# lists as values for tuple 
t1=([1,2],[5,-6],[4,3])
t1[0]
t1[0][1]
t1[1][0]=99

# doent work insertion, remove & update for tuple as its immutable
t1=([1,2],[5,-6],[4,3])
t1.insert(2,(5,5))  
t1
t1.remove((5,5))
t1[1]=[11,22]


# Cancatination and repeatation for tuple 
t1=(1,2,3)
t2=(4,5,6)
t1+t2
t1*3

# deletion of single element in list and total list deletion
del t1[1]  # can'r perform as this is an edit to the tuple ( immutable)
del t1