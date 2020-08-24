# Overloading operators (Ad-hoc Polymorphism) - practice on all magic functions 

class Vector:
    def __init__(self, a, b): 
      self.a = a 
      self.b = b 
    def __str__(self): 
      return 'Vector::::: (%d, %d)' % (self.a, self.b) 
    
    def __add__(self,other): 
      return Vector(self.a + other.a, self.b + other.b) 

# magic functions 
v1 = Vector(3,2) 
v2 = Vector(9,-5) 
print (v1 + v2)     
print(v1)

