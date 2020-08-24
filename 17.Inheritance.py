# Inheritance- 2 types in Python 1. Multiple and 2. Multilevel

#Multiple in heritance
# A,B  ===> C
class A:
    def displaya():
        print('parent class: A display function')

class B:
    def displayb():
        print('parent class: B display function')

class C(A,B):
    def displayc():
        print('child class: C display function')

a=A()
b=B()
c=C()


# A==>B and A ===> C
class A:
    def displaya():
        print('parent class: A display function')

class B(A):
    def displayb():
        print('parent class: B display function')
        
class C(A):
    pass

a=A()
b=B()
c=C()

#********************************************
# Multilevel Inheritance - A==> B ==> C

class A:
    def displaya():
        print('parent class: A display function')

class B(A):
    def displayb():
        print('parent class: B display function')
        
class C(B):
    pass

a=A()
b=B()
c=C()
        