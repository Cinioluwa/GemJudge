def merge_sort_inplace(arr, start, end):
    """
    Recursively sorts the subarray of 'arr' defined by the indices [start, end).
    This function works in-place by using indices instead of slicing the array.

    Parameters:
    - arr: the list to be sorted.
    - start: the starting index (inclusive) of the subarray.
    - end: the ending index (exclusive) of the subarray.

    Base Case:
    If the subarray has 0 or 1 element (i.e., end - start <= 1), it is already sorted.
    """
    # Base case: if the subarray has 1 or 0 elements, no need to sort further.
    if end - start <= 1:
        return

    # Find the midpoint of the subarray.
    mid = (start + end) // 2

    # Recursively sort the left half [start, mid) and the right half [mid, end)
    merge_sort_inplace(arr, start, mid)
    merge_sort_inplace(arr, mid, end)

    # Merge the two sorted halves back into the original list.
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    """
    Merges two sorted subarrays of 'arr' into a single sorted subarray.
    The left subarray is from [start, mid) and the right subarray is from [mid, end).

    This function uses a temporary list to merge the elements in order and then
    copies the merged list back into 'arr' for the indices [start, end).

    Parameters:
    - arr: the original list containing the subarrays.
    - start: starting index (inclusive) of the left subarray.
    - mid: ending index (exclusive) of the left subarray and starting index of the right subarray.
    - end: ending index (exclusive) of the right subarray.
    """
    # Temporary list to hold the merged output.
    temp = []

    # Pointers for each subarray:
    i = start  # Pointer for left subarray
    j = mid  # Pointer for right subarray

    # Merge the two subarrays into 'temp'
    while i < mid and j < end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Append any remaining elements from the left subarray (if any)
    while i < mid:
        temp.append(arr[i])
        i += 1

    # Append any remaining elements from the right subarray (if any)
    while j < end:
        temp.append(arr[j])
        j += 1

    # Copy the merged list back into the original array.
    # This copies elements into the section defined by [start, end).
    arr[start:end] = temp


# Example usage:
if __name__ == "__main__":
    alist = [54, 24, 14, 63, 29, 100, 95, 20, 305, 58]
    print("Original list:", alist)

    # Call the merge sort function on the entire list.
    merge_sort_inplace(alist, 0, len(alist))

    print("Sorted list:", alist)
