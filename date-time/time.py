#!/usr/bin/python3
import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#!/usr/bin/python3
import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)

import datetime
 
a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # '20170405'
 
today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '04/05/2017' 
print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 2017-04-05-00.18.00
