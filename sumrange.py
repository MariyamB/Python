import numpy as np
from pip._vendor.distlib.compat import raw_input

#makearange = lambda a: np.arange(int(a[0]),int(a[1]),int(a[2]))
#x = makearange(raw_input('Enter start,stop,increment: ').split(','))
start=int(input("Enter the start range:"))
stop=int(input("Enter the stop range:"))
next=start
sum1=0
for i in range(stop):
    next=start+1
    sum=start+sum1
    start=next
    sum1=sum
    if(start>stop):
       break
print("Sum of the range of numbers is:",sum)