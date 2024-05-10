import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('TKAgg')

def insertionsort(a):
    n = len(a)
    for i in range(1,n):
        k = a[i]
        j = 1-1
        while j>=0 and a[j]>k:
            a[j+1] = a[j]
            j = j-1
            a[j+1] = k

x=[10, 25,48,72,51,34,69,90]
print("Before Sorting",x)
insertionsort(x)
print("After sorting",x)

x=list(range(1,100))
plt.plot(x, [y*y for y in x])
plt.title("insertion sort Time Complexity is O(n^2)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()