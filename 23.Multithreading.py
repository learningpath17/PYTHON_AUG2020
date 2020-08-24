# Normal programming

import os
os.getcwd()
os.chdir('C:\\Venkat\\Personal\\Trainings\\Python')
os.getcwd()

# File modes(r,r+,w,w+,a,a+,etc..)
# Open a file from mentioned path
ft1=open('square.txt','w')
ft2=open('cube.txt','w')

import time
def cal_square(numbers):
    for n in numbers:
        time.sleep(1)
        s=str(n*n)
        ft1.write(s)
        print('Square:', n*n)

def cal_cube(numbers):
    for n in numbers:
        time.sleep(1)
        c=str(n*n*n)
        ft2.write(c)
        print('Cube:', n*n*n)

array=[2,3,4,5]
time1=time.time()
cal_square(array)
cal_cube(array)

ft1.close()
ft2.close()

print('Processing time: ', time.time()-time1)

# By using multithreading 

ft1=open('square.txt','w')
ft2=open('cube.txt','w')


import time
import threading

def cal_square(numbers):
    for n in numbers:
        time.sleep(1)
        s=str(n*n)
        ft1.write(s)
        print('Square:', n*n)

def cal_cube(numbers):
    for n in numbers:
        time.sleep(1)
        c=str(n*n*n)
        ft2.write(c)
        print('Cube:', n*n*n)

array=[2,3,4,5]
time1=time.time()
threadLock=threading.Lock()
threads=[]
#cal_square(array)
#cal_cube(array)
t1=threading.Thread(target=cal_square,args=(array,))
t2=threading.Thread(target=cal_cube,args=(array,))
t1.start()
t2.start()

threads.append(t1)
threads.append(t2)
for t in threads: 
    t.join()

ft1.close()
ft2.close()
print ('Multi threading completed:::::')
print('Processing time: ', time.time()-time1)
