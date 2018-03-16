import random
import math
#1.Read N vales from the user
N = int (input ("Enter number of throws : "))
print (N)

#2.Intialize the accumulator which is in the circle
inCircle=0
piEstimate=0

#Generate random number upto 1000
for count in range(1,N+1):
    pass# do nothing statement

    #print(count)
    x=random.uniform(-1.0,1.0) #0.0
    y=random.uniform(-1.0,1.0) #0.0

    if math.sqrt(x*x + y*y) <= 1.0:
        inCircle=inCircle+1
        piEstimate=4.0*inCircle/(count+1)
result=piEstimate-math.pi
print("Final Estimate is :", piEstimate)
print("Error is : ",abs(result))