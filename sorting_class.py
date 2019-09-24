# It's a class that can sort 1D list, sublists of a 2D list based on
#   a specific index
import random


def merge(unsorted_list, start, mid, end):
    start_index = start
    mid_index = mid + 1
    sorted = [0] * (end - start + 1)
    for x in range(end - start + 1):
        if start_index > mid:  # first part of the list comes to end
            sorted[x] = unsorted_list[mid_index]
            mid_index += 1
        elif mid_index > end:  # second part of the list comes to end
            sorted[x] = unsorted_list[start_index]
            start_index += 1
        elif unsorted_list[start_index] < unsorted_list[mid_index]:
            sorted[x] = unsorted_list[start_index]
            start_index += 1
        else:
            sorted[x] = unsorted_list[mid_index]
            mid_index += 1
    for x in range(end - start + 1):
        unsorted_list[start] = sorted[x]
        start += 1


# merge sort for 1D list
def merge_sort(unsorted_list, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(unsorted_list, start, mid)
        merge_sort(unsorted_list, mid + 1, end)
        merge(unsorted_list, start, mid, end)


"""
# test
test_list = []
for x in range(11):
    test_list.append(random.randrange(11))
merge_sort(test_list, 0, 10)
print(test_list)

"""


"""
merge sort for a 2D list sublists based on a specific index
This is really inefficient. Recording the index change of "index_list" may be
    faster, but I don't wanna write another sorting algorithm again, so...
    
"""
def sort_2d(unsorted_2d_list, start, end, specific_index):
    index_list = []
    for i in range(len(unsorted_2d_list)):
        index_list.append(unsorted_2d_list[i][specific_index])
    merge_sort(index_list, 0, len(index_list) - 1)
    for a in range(len(index_list)):
        for b in range(a, len(index_list)):
            if unsorted_2d_list[b][specific_index] == index_list[a]:  # swap the indexes
                unsorted_2d_list[b], unsorted_2d_list[a] = unsorted_2d_list[a], unsorted_2d_list[b]
                break


"""
# test
test_list2 = []
for x in range(1, 11):
    test_list2.append([0, random.randrange(1, 11)])
sort_2d(test_list2, 0, 9, 1)
for j in range(len(test_list2)):
    print(test_list2[j][1], end=" ")

"""
