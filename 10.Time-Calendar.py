# Time and Calendar
import time

#No of tricks(seconds) from 12.00 am, 1 st Jan 1970
tricks = time.time()
print('no of tricks :',tricks)

# check the time difference use for pgm execution/response time etc..
t1=time.time()
t2=time.time()
t2-t1

t=time.localtime()
t
type(t)
t[0]
t[6]

time.asctime( time.localtime(time.time()) )
# for the above same we can use time.asctime()
# asctime is to get the time in readable format.
time.asctime()

time.timezone

time.tzname 
#****************************************************************

import calendar
calendar.calendar(1250)

calendar.isleap(2016)
calendar.monthcalendar(2018,8)
calendar.firstweekday()
t=calendar.weekday(2018,8,1) 
t
if t == 0:
    print (' Monday')
elif t ==1:
    print ('Tues day')
    

