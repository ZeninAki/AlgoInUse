# Given an array arr[] of n elements, write a function to search a given element x in arr[].

def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


l = [2, 4, 5, 19]
need = 4
width = len(l)

res = search(l, need, width)
if res == -1:
    print('Element does not exist')
else:
    print(f'Element is at index {res}')

# This can be improved by finding both left and right at the same time
# in case there is a chance that the element is at the end of the array

# One alternate way to implement this is recursive

# Time complexity O(n)
# Auxiliary space O(1)
