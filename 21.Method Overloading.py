# Python doent support method overloading like C++ 
# If we write the methods with different argument but python will consider only latest one.
# Example

def addition(a,b):
    print(a+b)

def addition(a,b,c):
    print(a+b+c)

add(3,4) 

# But we can code the function behaviur differently as below.   
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello ')

# Create instance
obj = Human()

# Call the method with out parameter
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')


