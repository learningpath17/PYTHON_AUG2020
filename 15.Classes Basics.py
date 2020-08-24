class Sample:   
    def dips():
        print('it is my first class defination')
        
ins1 = Sample()
ins2 = Sample()


ins1.disp()         
        
        
        
        
        


# Class defination , __init__ & __del__
class Studclass:
   'student class'
   stdcount = 0 
   def __init__(self, name, marks): 
       self.name = name 
       self.marks = marks 
       Studclass.stdcount += 1 
       print('I am at Initial funcction')
       print (Studclass.stdcount)
       print(name,'   '   , marks)
    
   def dispcnt(self): 
       print ("Total Students %d" % Studclass.stdcount) 
       print('I am at display count funcction')
   
   def dispstd(self):
       print('Name: ', self.name,'Marks: ', self.marks)
       print('I am at display student function')
   
   def __del__(self): 
      class_name = self.__class__.__name__ 
      print (class_name, "destroyed")


std1=Studclass('abhi',300) 
std2=Studclass('rithwik',320)


std1.dispcnt()
std1.dispstd()
std2.dispstd()


del std1  
std2= Studclass('Rithwik', 320) 

std1.dispstd() 
std1.dispcnt()     
#		print ("Name : ", self.name,  ", marks: ", self.marks)
std1.age =8
std1.age
std1.age =9
del std1.age

# Instances indentification by using id number
id(std1)
id(std2)
std3=std1
id(std3)



# some of basic class functions 
print('stdclass.__doc__:', Studclass.__doc__) 
print('stdclass.__name__:', Studclass.__name__ )
print('stdclass.__module__:', Studclass.__module__) 
print('stdclass.__bases__:', Studclass.__bases__) 
print('stdclass.__dict__:', Studclass.__dict__)




