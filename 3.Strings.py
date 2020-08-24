# Strings defination - alpha, numeric or alpha numeric combination with sigle or double quotes

s1='10'
s2='xyz'
s3='hyd-72'

# String operations
st1='hyderabad.mumbai'
st2='chennai'
str3='   '

# slicing on strings by using indexes whcih starts from 0 for forwad direction and
# for backward direction indexe starts from -1
st1[0]       # return first value in the string
st1[3:6]     # return the values from index 3 to index 5 (end index not include)
st1[-2]      # return value from last 2 nd as its backward reading
st1[2:]      # return all the values from index 2 till end of the string
st1[-6:-1]   # return string from -6 index to -2 index
st1[3] = '77'  # string variable doesn't support to edit the values at specific index.  

# functions on strings
st1='hyderabad.mumbai'

st1='123'
st2=123

len(st1)

st1.isdigit()
st1.isnumeric()
st1.islower()
st1.isupper()
st1.isalpha()
st1.isalnum()

#check the object type against target type
x=10
isinstance(x,int) 


st1.capitalize()
st1.upper()
st1.lower()
st1.center(20)
st1.center(20,'@')
st1.zfill(20)
t='8765'
t.zfill(20)

st1.count('a') # return no of times substring repeation in main string.
st1.count('a',2,7)  # count substring only inmentioned range


st1.find('k') # retuns the index where the substring is find first else returns -1 
st1.find('b',3,6) # find substring only in mentioned range


# cancatination and repeatation fo strings
fname='John'
lname='Kilner'

fname+lname
fname+ ' ' +lname
fname * 2


# tab space, alert , new line in a string

letter = 'dhjkfdgkjhdgjk\t hdfhdsgh\b dgdsg \ajhjdhsgkj \n'
letter 
st1='\a'
print('student name:', letter,st1,'end')


# type conversation 

#from string to int   
x='20.98'
n= int(x)
# int to string
a=10
st1=str(a)

# String dispaly formats.
age=30
name='venkat'
print(' My name is: {}, age is: {}'.format(name,age))
