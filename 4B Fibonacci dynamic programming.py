n= int(input("Enter a Number"))
a=0
b=1
if n<=0:
    print("The output of your input is: ",a)
else:
    print(a,b,end="")
    for x in range(2,n):
        c=a+b
        print(c,end="")
        a=b
        b=c