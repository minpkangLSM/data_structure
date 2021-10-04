def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right :
        mid = (left+right)//2
        if arr[mid] == target :
            return 1
        elif arr[mid] > target :
            right = mid-1
        else :
            left = mid+1

    return 0

a = [6, 4, 9, 3, 8, 1]
a.sort()
results = binary_search(a, 10)
print(results)