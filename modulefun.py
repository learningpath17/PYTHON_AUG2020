#print ("program for Module program calling")
#a=10
# add function
def add(a,c,b):
    sum = a+b+c
    print ('in function sum : ' , sum )
    return sum

# print function
def pnt():
    print('hello first function')
    return 

# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

