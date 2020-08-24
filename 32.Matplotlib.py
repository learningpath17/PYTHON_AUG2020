from matplotlib import pyplot as plt

#%matplotlib qt

# basic line graphs 
plt.title('Hyderabad population by Year')
plt.xlabel('Year')
plt.ylabel('Population in Lakhs')

plt.plot([2000,2005,2010,2015],[80,94,110,132])

plt.show()

# style for the plots

from matplotlib import style 
style.use('ggplot')
x1=[2000,2005,2010,2015]
y1=[80,94,10,32]

x2=[2000,2005,2010,2015]
y2=[90,104,20,42]

plt.plot(x1,y1,'g',label='Hyderabad',linewidth=5)  # x,y coordinates,color, label, line width
plt.plot(x2,y2,'c',label='Mumbai',linewidth=5)
plt.title('Population for HYD and MUM')
plt.xlabel('Year')
plt.ylabel('Population') 
plt.legend()    # to setting up labels
plt.grid(True,color='k')  # back group grid with black color
plt.show() # generate graph

# bar Graphs

from matplotlib import pyplot as plt
x1=[1,3,5,7,9]
y1=[10,14,8,22,7]

x2=[2,4,6,8,10]
y2=[13,4,20,12,33]

plt.bar(x1,y1,color='r',label='Hyderabad')  # x,y coordinates,color, label, line width
plt.bar(x2,y2,color='g',label='Mumbai')
plt.title('Population for HYD and MUM')
plt.xlabel('Year')
plt.ylabel('Population') 
plt.legend()    # to setting up labels
plt.grid(True,color='k')  # back group grid with black color
plt.show() # generate graph

#histograms
from matplotlib import pyplot as plt
list1=[2,4,56,78,22,33,4,6,77,88,33,44,22,12,13,16,17,49,50,66,85]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(list1,bins,histtype='bar',rwidth=0.7,label='WOW',color='g')

plt.xlabel('Age group')
plt.ylabel('Population') 
plt.legend()    # to setting up labels
plt.grid(True,color='k')  # back group grid with black color
plt.show() # generate graph

#scatter plots

from matplotlib import pyplot as plt
x=[2,5,8,3,6]
y=[4,6,2,5,8]

plt.scatter(x,y,label='Scatter',color='g',s=100,marker='*')

plt.xlabel('Age group')
plt.ylabel('Population') 
plt.legend()    # to setting up labels
plt.grid(True,color='k')  # back group grid with black color
plt.show() # generate graph

# Area plots / stag plots
from matplotlib import pyplot as plt
days=[1,2,3,4,5]
sleeping=[7,8,9,6,5]
eating=[1,2,1,3,2]
playing=[3,4,2,6,1]
working=[4,5,8,3,9]
plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.tittle('stackplot')
plt.xlabel('day')
plt.ylabel('Activities') 
plt.legend()    # to setting up labels
plt.grid(True,color='k')  # back group grid with black color
plt.show() # generate graph

# Pie plots

from matplotlib import pyplot as plt
slices=[7,2,2,13]  # percentage of the Pie.
labs=['IBM','TCS','WIPRO','INFY']
col = ['m','c','r','g']
plt.pie(slices,labels=labs,colors=col,startangle=90,shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%')

plt.title('Pie Plot')
plt.legend()    # to setting up labels
#plt.grid(True,color='k')  # back group grid with black color
plt.show() # generate graph

# Multiple plots at single time or in single page
from matplotlib import pyplot as plt

plt.subplot(211) # Hrizental , vertical and This graph number.
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
plt.subplot(212)
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
plt.show()
