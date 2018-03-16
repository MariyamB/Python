import math
import random

numTerms= int(input("enter the number of terms :"))
sign=1.0
result=0

for count in range(numTerms):
    sign=-sign
    result=result+sign/(2.0+count+1.0)

print(4*result)
print("Deviation from pi is:" +str(math.pi-result))