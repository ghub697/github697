import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

def bubbleSort(a):
    n = len(a)
    temp = False

    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return

a=[10,12,20,30,40,50,60,70,80]
bubbleSort(a)
print("Sorted array is :")
for i in range(len(a)):
    print("% d" % a[i], end="")

x=list(range(1,100))
plt.plot(x,[y*y for y in x])
plt.title(" bubblesort - time Complexity is 0(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
