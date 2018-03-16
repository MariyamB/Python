import random
x=random.uniform(1.0,6.0)
y=random.uniform(1.0,6.0)
print("The values of x and y are:",x,y)
print("The sum of the values of x and y is :",x+y)

n=10
for i in range(0,n+1):
 print(i," ")


#Method 1
import random
one = random.randint (1, 6)  # random.randrange(0,7) also ok
two = random.randint (1, 6)
print (one + two)

#Method 2
import random
one = random.randrange (1, 6)  # random.randrange(0,7) also ok
two = random.randrange (1, 6)
print (one + two)