# default Exception
n= int(input('Please enter a number: '))
print(n)

# to find the exception
try:
    n = input("Please enter an integer: ")
    n = int(n)
except Exception as e:
    print('Exception occured : ', e)

print ('value: ' , n)    

# default Exception handling -single exception

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Given value is not Interger , enter value with out decimals again ...")

print("Great, you successfully entered an integer!")

# default Exception handling -single exception with else

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
    except ValueError:
        print("Given value is not Interger , enter value with out decimals again ...")
    else:
        print('Entered value is Interger - good bye..!')
        break
# Multiple exceptions handling

import os
os.getcwd()
os.chdir('C:\\Venkat\\Personal\\Trainings\\Python')
try:
    ft=open('test.txt','w')
    ft.write('xyz')
    a=246/0
except IOError:
    print('IO eeror on file')
except ZeroDivisionError:    
    print('this is wrong division')
else:
    print('this is sucessfully executed')
finally:
    print('this is finall statement')

ft.close()


# nested try blocks for exception handling

try: 
   ft1 = open("testfile1", "w") 
   ft1.write("test file-1!") 
   try: 
       ft2 = open("testfile2", "w") 
       ft2.write("test file-2!") 
   except IOError: 
       print ("inside file handling Error") 
   else:
       print('Inside else part executed')
   finally: 
      print ("Going to close inside the file") 
      ft2.close() 
except IOError: 
   print ("Outside file handling Error") 
else:
       print('Outside else part executed')
finally: 
      print ("Going to close out file the file") 
      ft1.close() 

# Exception handling with Assert key word 
def KelvinToFahrenheit(Temperature): 
   assert (Temperature >= 0),"Colder than absolute zero!" 
   return ((Temperature-273)*1.8)+32 
 
print (KelvinToFahrenheit(273)) 
print (int(KelvinToFahrenheit(505.78))) 
print (KelvinToFahrenheit(-5)) 


# User define exceptions 

class userexception(Exception):
    'base exception class'
    pass
class userexp1(userexception):
    pass
class userexp2(userexception):
    pass

number = 70
try:
    if number > 100:
        raise userexp1
    elif number < 40:
        raise userexp2
        
except userexp1:
    print('not acceptable marks pls check')

except userexp2:
    print('less marks & no rank')
else:
    print ('genearted the rank')
    
finally:
    print('successfully done')    
    
    
    
    
