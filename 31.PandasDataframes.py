#In Pandas Series is one dimentional data structures
#Data frames are two dimentional data structures.

import pandas as pd 
 
col1 = [10,20,30,40] 
col2 = ['abc','def','xyz','pqr'] 
col3 = [0,0,0,0] 
 
#creating data frame 
df1 = pd.DataFrame({'pid':col1, 
 'pname':col2,'survived':col3}) 
df1.shape 
df1.info() 
df1.describe() 
df1.head(2) 
df1.head()      # first 5 rows
df1.tail()      # last 5  rows 

df1['col4'] = 0  # creating new column with all values as 0

#access frame content by column/columns 
df1.pid 
df1['pid'] 
df1[['pid','pname']] 


#dropping a column 

df2 = df1.drop('survived',1) 

#slicing rows of frame 
df1[0:2] 
df1[0:4] 
df1[0:] 
df1[:2] 
df1[-2:] 

#filtering rows of dataframe by condition 
type(df1.pid > 20) 
df1[df1.pid>20] 
 
#selecting subsets of rows and columns 
df1.iloc[0:2,] 
df1.iloc[[0,2],] 
df1.iloc[0:2,0] 
df1.iloc[0:2,[0,2]] 
df1.loc[0:2,['pname']] 
 
# Another example
import pandas as pd
data={
      'students':['a','b','c','d','e','f'],
      'maths':[99,94,93,98,97,93],
      'science':[96,91,96,94,98,96],
      'sports':['baseball','cricket','tt','badminton','tt','boxing']
      }

std=pd.DataFrame(data,columns=['students','maths','science','sports'])
print(std)


list1= [1,2,3,4,5,6]
ldata=pd.DataFrame(list1,columns=['Ranks'])
print(ldata)

list1= [[1,2,3,4,5,6],[3,4,5,7,8,9]]
ldata=pd.DataFrame(list1,columns=['l1','l2','l3','l4','l5','l6'])
print(ldata)

#grouping data in data frames 
import os
os.getcwd()
os.chdir('C:\\Venkat\\Personal\\Trainings\\Python')
os.getcwd()

import pandas as pd
#headers=['Name','Title','Department','Salary']
chicago=pd.read_csv('ChicagoEmployees.csv',header=None) # reading with header / with out header header=1
chicago.shape
chicago.info()
chicago.describe()
#chicago

print(chicago.head())
dept=chicago.groupby(2)
dept.count().head()
#dept.size()
dept.size().head()

