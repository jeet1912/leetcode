
def binarySearch(arr,target):
    l = 0
    r = len(arr) - 1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            #do something
            pass
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    #target not in arry, l is the insertion point
    return l

# Duplicate elements 
# if target appears multiple times in the array

# Left most index
def binary_search_L(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

# Right most index
def binary_search_R(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] < target:
            right = mid
        else:
            left = mid + 1
    return left
