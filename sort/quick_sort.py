# Quick sort : 21.09.26.
unsorted = [5, 1, 4, 2, 3, 10, 11, 8, 9, 12, 13, 6, 15]

def partition(list, left, right):
    low = left
    high = right+1
    pivot = list[left]
    while True :
        # low
        while True :
            low += 1
            if pivot <= list[low] or right < low : break
        # high
        while True :
            high -= 1
            if pivot >= list[high] or high < left : break
        if low < high :
            temp = list[low]
            list[low] = list[high]
            list[high] = temp
        if low > high : break
    temp = list[left]
    list[left] = list[high]
    list[high] = temp
    return high

def quick_sort(list, left, right):
    if left < right :
        p = partition(list, left, right)
        quick_sort(list, left, p-1)
        quick_sort(list, p+1, right)
    return list

st = quick_sort(unsorted, 0, len(unsorted)-1)
print(st)