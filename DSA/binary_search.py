def binary_search(arr, target):
    #iterative binary search
    #first and last are index positions
    first = 0
    last = len(arr) - 1 #index position= actual length - 1 since indexing starts from 0 while counting starts from 1

    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return None
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)