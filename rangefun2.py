
N = 10
for num in range(1,N+1):
    print (num,end=' ') # end='' keeps loop output on same line
    #print () # start new line

print()
for num in range(1,N):
    if(num%2==1):
     print (num,end=' ') # end='' keeps loop output on same line
    #print () # start new line

print()
for num in range(0,N):
    print (N-num,end=' ') # end='' keeps loop output on same line
    #print () # start new line

print()
num1=0
for num in range(0,N):
    x= N - num1
    if(x>0):
     print (x,end=' ') # end='' keeps loop output on same line
     num1=num1+3
    #print () # start new line

print()
num1=1
for num in range(N):
    print (num1,end=' ') # end='' keeps loop output on same line
    num1=num1+4
    #print () # start new line

print()
num1=47
for num in range(0,N):
     if(num1>0):
      print (num1,end=' ') # end='' keeps loop output on same line
      num1=num1-46
    #print () # start new line