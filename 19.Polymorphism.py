# Example for Polymorphism (look like method overriding)

class Father():
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def disp_name(self):
         print('Father :' + self.fname + '  ' + self.lname)
    def disp_age(self):
         print('age is : ' + self.age)
class Son(Father):
    def disp_name(self):
        print('Son :' + self.fname + '  ' + self.lname)
class Daughter(Father):
    def disp_name(self):
        print('Daughter :' + self.fname + '  ' + self.lname)

f=Father('John','Kilner',53)
s=Son('Mark','Jo',30)
d=Daughter('Nicky','Cary',22)

# Father details
f.disp_name()
f.disp_age()
#son details
s.disp_name()
s.disp_age()
# daughter details
d.disp_name()
d.disp_age()    

# Operator overloading ( polimorphism ) 
a=10
b=20

print(a+b)
c='hyd'
d='-72'
print(c+b)

# Polimorphism another type -duck typing.
class Circle:

    def corners(self):
        print("circle has no corners")
    
    def area(self):
        print("aread is pi(r**2) ")

class Rectangle:

    def corners(self):
        print("circle has 4 corners")
    
    def area(self):
        print("aread is length*width ")

# common function to use class methods
def corners_count(shape):
        shape.corners()

#instances / objects
cir = Circle()
rec = Rectangle()
# passing the object
corners_count(cir)
corners_count(rec)

  