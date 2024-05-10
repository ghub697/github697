import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('TKAgg')

def selection_Sort(a):
    n=len(a)
    for i in range(n):
        min=1
        for j in range(i+1,n):
            if (a[j] < a[min]):
                min=j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    return (a)

a=[10,25,48,72,51,34,69,98]
print("Before Sorting", a)
selection_Sort(a)
print("After sorting",a)

x=list(range (1,100))
plt.plot(x, [y*y for y in x])
plt.title("Selection Sort-Time Complexity is B(n/uB0b2)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()