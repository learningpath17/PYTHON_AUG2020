# Python program to demonstrate 
#Numpy - Numerical Python  
# basic array characteristics
l = [i for i in range(1,4)]
l

# instead of loops coding Numpy will help to process 
#Each element multiply by 3 by Using for loop 
for i in range(len(l)):
    l[i]*=3              
    
import numpy as np 
#Each element multiply by 3 by Using for 
arr = np.array([1,2,3])  
arr*=3

# Creating array object 
arr = np.zeros(4)
arr

# check each value in array
arr = np.arange(0,10)
arr>4

arr = np.array( [ 1, 2, 3])
arr.ndim,arr.shape,arr.size

# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 


# creating flot type array 
arr2=np.array([1,2,3,4],dtype=np.float64)
arr2
                 
                 
# two dimensional arrays
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
  
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 

# transformation - rows become columns and vicd versa

arr.transpose() 

# Another example

# Reshaping 3X4 array to 2X2X3 array 
arr = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
  
newarr = arr.reshape(2, 2, 3) 
  
print ("\nOriginal array:\n", arr) 
print ("Reshaped array:\n", newarr) 
  
# Flatten array 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = arr.flatten() 
  
print ("\nOriginal array:\n", arr) 
print ("Fattened array:\n", flarr) 

# arraays witth given range
np.linspace(0,10,5)
np.arange(0,10)
np.arange(0,10,3)

# arrays with random
np.random.standard_normal((2,4))  

# stacking vertical and horizantal
  
a=np.random.standard_normal((2,4))  
b=np.random.standard_normal((3,4))  
a
b
np.vstack((a,b))  # no of rows shd match for vertical
np.hstack((a,b)) # no of cols shd match for horizantal

c=np.random.standard_normal((3,5))  
np.hstack((b,c))

# to save array to a name and reload into program
a=np.random.standard_normal((2,4))  
np.save('test.npy',a)
a
# reload
al=np.load('test.npy')
al

# Image conversion & set the path to get the sample photo
import os
os.chdir('C://Venkat//Personal')
from skimage import io
photo = io.imread('House Wall.jpg')
type(photo)
photo.shape

import matplotlib.pyplot as plt
print(plt.imshow(photo))

# reverse of the pic (rows revers )
plt.imshow(photo[::-1])
# Mirro image (reverse fo columns)
plt.imshow(photo[:,::-1])

# Slice of the photo (zoom) or  only specific part of photo by using pixels
plt.imshow(photo[50:100,70:120])

# reducing pixels (quality by half)
plt.imshow(photo[::2,::2])

# masking of photos where > 100 all pixels will be replace with 250 and other <100 will be replace with 0 pixel.

photo_mask = np.where(photo>100,255,0)
plt.imshow(photo_mask)
# also all math/sats operation can perform- mean,median,min,max,covariance etc..
photo.mean()