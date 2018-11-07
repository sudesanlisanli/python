

def Buble_Sort(arr):
    for pass_ in range(len(arr)-1):
        for mov in range(len(arr) - 1 - pass_ ):
            if arr[mov] > arr[mov + 1]:
              temp = arr[mov]
              arr[mov] = arr[mov + 1]
              arr[mov + 1] = temp



array=[14,27,33,10,35,-1,45]
print("Array:   ")
print(array)
Buble_Sort(array)
print("Sorted array!")
print(array)
