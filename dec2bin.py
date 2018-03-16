def dec_to_bin(dec):

   if dec > 1:
       dec_to_bin(dec//2)
   print(dec % 2,end = '')


dec = int(input("Enter the number to be converted to binary:"))

dec_to_bin(dec)