num = int(input("enter number of floats: "))

a = 0.0
b = 0.0
c = 0.0
for d in range(num):
    e = float(input("enter next float: "))
    a = max(a, e)
    b = min(b, e)
    c = c + e
    print ("set breakpoint here...")
    # LOCATION 1:# list values of a, b, c, d, e at this point, each time through loop
    #Iteration 1:10101
    #Iteration 2:1 - 2 - 11 - 2
    #Iteration 3:3 - 2223
    #Iteration 4:3 - 4 - 24 - 4
    print (a)
    print (b)
    print (c / num)
    print ("set another breakpoint here...")
    #list final values of a, b, c, d, e
    #Iteration 1:10111
    #Iteration 2:1 - 2 - 12 - 2
    #Iteration 3:3-2233
    #Iteration 4:5-4345