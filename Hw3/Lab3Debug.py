number = int (input("Enter number of ints to process: "))

max_so_far = 0
#count=1
for count in range(number):

   next_int = int(input("Enter next integer: "))
   if(count>0):
    max_so_far = max(max_so_far,next_int) # note the built-in max()
   else:
    max_so_far=next_int
print("Largest entered is:", max_so_far)
