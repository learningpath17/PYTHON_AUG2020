# data / method -  Encapsulation/Abstraction /Hide 

# variable 
class Normalclass: 
   value = 10 
   
   def dispname(self): 
      self.value += 1 
      print (self.value) 
 
hc = Normalclass() 
hc.
hc.dispname()
hc.dispname()

hc.secretvalue
 
class Hideclass: 
   __value = 10 
   
   def dispname(self): 
      self.__value += 1 
      print (self.__value) 
 
c1 = Hideclass() 
c1.dispname()
c1.__value

c1._Hideclass__value



hc.dispname()
hc.dispname()
hc.__secretvalue
# normal calling
print (hc.__secretvalue) 
# secret variables (Abstract/hide) variables calling 
print (hc._Hideclass__secretvalue)

#**********************
# another example for methodsand variable

class Marks:

    def __init__(self):
        self.__totmarks = 200

    def disp(self):
        print("Total marks : {}".format(self.__totmarks))

    def changemarks(self, marks):
        self.__totmarks = marks
    
    def __rank(self):
        print ('rank of the student is here : 1')

c = Marks()
c.disp()

c.disp()

# change the price
c.__totmarks = 232
c.disp()

c._Marks__totmarks=400
c.disp()

# using setter function
c.changemarks(232)
c.disp()
c.__rank()  
c._Marks__rank()
