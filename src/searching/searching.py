def linear_search(arr, target):
    # Your code here
    # We simply loop over an array 
    # from 0 to the end or len(arr)
    for item in range(0, len(arr)):
        # We simply check if the item is equal 
        # to our target value
        # If so, then simply return the item
        if arr[item] == target:
            return item
    # If the target does not exist in our array
    # Return -1 which equates to not found
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # We need the beginning of the array
    # So we create a variable and start at zero
    start = 0
    # Next we need to find the end of the array
    # Create a variable use the length and - 1
    end = len(arr) - 1

    # Next we create a loop that runs as long at the start
    # and the end are NOT the same and start is LESS THAN
    # the value of end
    while start <= end:
        # Here we create the middle value 
        # We simply add the start + end and then divide
        # By two to find the median value or middle
        middle = (start + end) // 2
        # If our middle value is the target we are search for
        # simply return the middle value
        if arr[middle] == target:
            return middle
        # Else if the middle value is less than our target value
        # We do not need any of the array values before our middle
        # So we make the start our middle value + 1
        elif arr[middle] < target:
            start = middle + 1
        # Else if the middle is greater than the target
        # we work backwards and make our mid value
        # equal to our end value and subtract one
        else:
            end = middle - 1
    # If the target value is not in the array 
    # return -1, which is not found
    return -1  # not found