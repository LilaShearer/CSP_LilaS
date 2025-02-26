# Lila Shearer, Time of Day Python

import time
current_time = time.localtime()  
hour = current_time.tm_hour  

if hour > 0 and hour < 12:
    print("Good morning!\n")
elif hour >12 and hour <17:
    print("Good afternoon!\n")
else:
    print("Good night!\n")
