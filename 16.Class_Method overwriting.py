# Methos overwriting 

class Student:        # Parent class 
   def parinfo(self): 
      print ('Snt class mettudent info Parehod') 
 
class Subject1():  # Child class 
    
    def subinfo1(self):
        print('subject info method in child class')
    def childinfo1(self): 
      print ('student information Child class method') 


class Subject2(Student,Subject1):  # Child class 
    
    def subinfo2(self):
        print('subject info method in child class')
    def childinfo2(self): 
      print ('student information Child class method') 


c2 = Subject2()          # instance of child class
c2.

c = Subject()          # instance of child class
c.parinfo()



c.stdinfo()
p.stdinfo()

 
