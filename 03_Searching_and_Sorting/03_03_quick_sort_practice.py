"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    less = []
    more = []
    equal = []
    for element in array:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            more.append(element)
        else:
            equal.append(element)
    return quicksort(less) + equal + quicksort(more)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
# [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]