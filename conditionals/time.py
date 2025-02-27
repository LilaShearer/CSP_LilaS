# Lila Shearer, Time of Day Python

import time
#first instance of time in programming
first_time = time.gmtime() # This tells you what time it is in England 


#current time in seconds
current = time.time()
#print(current) #seconds since January 1 1970 because that's when computers started counting time.

#current date and time like we see it normally
now = time.ctime(current)
#print(now)

#get just a part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour
print(day, hour)



#or you can do it like this
import time
current_time = time.localtime()  
hour = current_time.tm_hour  
