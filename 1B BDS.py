import array as arr
A=arr.array ( 'i',[])
N=int (input ("enter the size of items:"))
for i in range (N):
    x=int (input ("enter the %d elements: "%1)) 
    A.append (x)
print ("Arrays elements:")
for i in range (N):
    print (A[i])