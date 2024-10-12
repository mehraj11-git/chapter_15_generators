# list vs generator 
# memory usage and time 
# when to use list and when to use generator

import time
# t1 = time.time()
l = [i**2 for i in range(10000000)]  #10 million
# t2 = time.time()
# print(t2-t1)
t1 = time.time()
g = (i**2 for i in range(10000000))  #10 million 
t2 = time.time()
print(t2-t1)
# we can check the data usage in task manager
#  now gonna analysis the time period of both
# first import the time
# then create a initial time variable and final time  after the code done
# we can directly write print(time.time - t1) we dont do better understanding
# look list takes time to print while generator doesnt takes any second to print
# 