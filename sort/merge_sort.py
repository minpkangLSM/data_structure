# merge sort : 21.09.26.
def merge_sort(array):
    if len(array) == 1 : return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i=0
    j=0
    k=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i+=1
            k+=1
        else :
            array[k] = right[j]
            j+=1
            k+=1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            k+=1
            j+=1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            k+=1
            i+=1

    return array

N = int(input())
unsorted = []
for i in range(N):
    unsorted.append(int(input()))
sorted = merge_sort(unsorted)
for a in sorted: print(a)

# # merge sort : 21.09.26.
# unsorted = [5, 1, 4, 2, 3, 10, 11, 8, 9, 12, 13, 6, 15]
# sorted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# def merge(list, left, mid, right):
#     i = left
#     j = mid+1
#     k = left
#     while i<=mid and j<=right :
#         if list[i] <= list[j] :
#             sorted[k] = list[i]
#             i+=1
#             k+=1
#         else :
#             sorted[k] = list[j]
#             j+=1
#             k+=1
#     if i > mid :
#         for idx in range(j, right+1):
#             sorted[k] = list[idx]
#             k+=1
#     else :
#         for idx in range(i, mid+1):
#             sorted[k] = list[idx]
#             k += 1
#     for l in range(left, right+1):
#         list[l] = sorted[l]
#
# def merge_sort(list, left, right):
#     mid = int((left+right)/2)
#     if left < right :
#         merge_sort(list, left, mid)
#         merge_sort(list, mid+1, right)
#         merge(list, left, mid, right)
#     return list
#
# sorted = merge_sort(unsorted, 0, len(unsorted)-1)
# print(sorted)