def fib4(n):
    if n<=1:
        return n
    else:
        return(fib4(n-1)+fib4(n-2))

x=int(input("Enter n number="))
print("Fibonacci Sequence")
for i in range(x):
    print(fib4(i))


