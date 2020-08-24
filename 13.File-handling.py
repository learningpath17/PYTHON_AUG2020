import os

import math as mt

 
mt.ceil(34.67)

os.getcwd()
os.chdir('C:\\Venkat\\Personal\\Trainings\\Python')
os.getcwd()

# File modes(r,r+,w,w+,a,a+,etc..)
# Open a file from mentioned path
ft=open('date1209.txt','w')

# Write a file
ft.write('line-1')

#close a file 
ft.close()

ft=open('date1209.txt','w')
ft.write('line-2')
ft.write('line-3')
ft.close()

# read full file 
ft=open('date1209.txt','r')
ft.read()
ft.close()

# read file content only specific length data
ft=open('date1209.txt','r')
ft.read(4)
ft.close()

# read total line at a time
ft=open('date1209.txt','r')
ft.readline()

# write multiple lines at a time
seq=['line-1\n','line-2\n']
ft=open('testfile2108.txt','r+')
ft.write('line-6')
ft.writelines(seq)
ft.write('\n')
ft.close()



# Other file functions
ft=open('date0808.txt','r+')
ft.tell()   # position of the control to read a file position
ft.read(1) 
ft.tell() 
ft.seek(0,0)   # to set the position
ft.tell()
ft.close()
ft=open('date0808.txt','w')
ft.write('line-5')
ft.close()

# to know whether file is closed or not.
ft.closed


ft=open('date0808.txt','r')
ft.seek(0,0)   # to set the position
next(ft)
ft.close()

# other file functions to know about file
ft.closed
ft.name
ft.mode
ft.fileno()

ft=open('date1213.txt','w+')
ft.write('hyderabad')
ft.close()


ft=open('date1213.txt','r+')
ft.read(3)
ft.read(2)

ft.read()
ft.truncate()
ft.close()


ft=open('test.txt','a+')
ft.write("end")
ft.read()
ft.read(10)
ft.close()
ft=open('test.txt','r+')
ft.readline()
ft.readlines()
ft.close()
ft=open('test.txt','r+')
print(ft.readline())
ft.flush

# Line by line read:
for i in open('planets.txt'):
    print(i, end='')
    