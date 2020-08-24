# Dictionary defination 
dict1 = {'name': 'Abhi','class': 2,'section':'c','rank':3}
dict1
dict1['name']    # get the values by using key as index
dict1['rank']

dict1['rank']=2    # update the value for given key
dict1['School']='DPS' # add new item (key and value)

del dict1['class']   # delete the item (key and value) by giving key

dict1.clear() # clear total dictionary
dict1

del dict1   # delete total dictionary
dict1

# get the value by using key with get function  
dict1 = {'name': 'Abhi','class': 2,'section':'c','rank':3}
dict1['name']
dict1['area']

dict1.get('name','not available name')
dict1.get('area','not available name')

l1=[1,2,3]
t1=('xy',34,67,33)
# dict2 creates with l1 values as keys and given values are values 
dict2=dict.fromkeys(l1,['xy','z'])
dict2

# function on dictionaries
dict1.keys()
dict1.values()
dict1.items()
dict1.clear()
dict1.get('name1','Not found')
dict2=dict.fromkeys([1,2,3,4],'DPS')
dict2=dict.fromkeys([1,2,3,4],{1:45})
dict1.update(dict2)
dict2

#prepare a dictionary with two different lists.
l1=[1,2,3,4,5]
l2=['a','b','c','d']
dict2=dict(zip(l1,l2))
dict2

# create a list with list of identical list items as keys and their occurance as value. 
l=['a','b','a','c','b','a','d','d','c','b']


dict1={i:l.count(i) for i in l }
dict1


import copy
li1 = [1, 2, [3,5], 4]
li2=copy.copy(li1)
li1
li2
li1[2][0]=7
li1
li2

#Deep copy
li1 = [1, 2, [3,5], 4]
li2=copy.deepcopy(li1)
li1
li2
li1[2][0]=7
li1
li2
dict1.values()
dict1.update(dict2)
dict2
dict1

# Set variable 
a={1,2,3,4,5}
a
type(a)
x=set('Pyhton Program')
x
y=set(['red','yello','blue'])
y
