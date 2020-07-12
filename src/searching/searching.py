def linear_search(arr, target):
    # Your code here
    for item in range(0, len(arr)):
        if arr[item] == target:
            return item

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return -1  # not found