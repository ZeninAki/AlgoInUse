# Given an array arr[] of n elements, write a function to search a given element x in arr[].
# This can only be done if the array is sorted
import math


def jumpSearch(arr, x, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1


a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
need = 55
ln = len(a)

ind = jumpSearch(a, need, ln)

if ind != -1:
    print(f'Element is at index {ind}')
else:
    print('Element does not exist')

# The optimal size of the block should be (√n) which make the time complexity to be O(√n)

# The time complexity of Jump search is between Linear search (O(n)) and Binary search (O(logn))

# Binary search is better than jump search but jump search will traverse back only once ( while
# binary search can take logn jump ). So in a system where binary search is costly, we can use the jump search


