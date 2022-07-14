# Given an array arr[] of n elements, write a function to search a given element x in arr[].
# This can only be done if the array is sorted

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1


a = [1, 2, 3, 4, 5, 6, 10, 100, 1000]
need = 10

res = binarySearch(a, 0, len(a)-1, need)

if res != -1:
    print(f'Element is at index {res}')
else:
    print(f'Element does not exist')

# By using recursive, the auxiliary space is O(logn) but if you use the iterative way
# which is the alternate, the auxiliary space can be O(1)

# Here we using [ mid = low + (high-low) / 2 ] but not [ mid = ( low + high ) / 2 ]
# because it can cause an overflow if both value are significantly higher. This can also be applied to
# merge sort and divide-and-conquer algorithms

# Time complexity O(logn)
# Auxiliary space O(1) if iterative else O(logn) if recursive

