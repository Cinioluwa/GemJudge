def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    O(kn log n)  time complexity
    """

    if len(list) <= 1:
        return list #Stopping condition, naive sorting

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half) #Remember recursion?

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    :param list:
    :return: two sublists- left and right

    Takes overall O(k log n) time complexity
    """

    mid = len(list) // 2
    left = list[:mid] #This slice operation takes O(k) where k is the slice size
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merge two lists(arrays), sorting them in the process
    :param left:
    :param right:
    :return: a new merged list

    O(n) - n number of sort steps or merges
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i]) #If the 1st value in the left list is less than 1st value in the right list, place it at the start of the new list 'l'
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left): #Incase there's an odd number of elements in the list and there's still stuff left in the left list not moved over to l
        l.append(left[i])
        i += 1

    while j < len(right): #Incase there's an odd number of elements in the list and there's still stuff left in the right list not moved over to l
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list [1] and verify_sorted(list[1:])


alist = [54, 24, 14, 63, 29, 100, 95, 20, 305, 58]
l = verify_sorted(merge_sort(alist))
print(l)

