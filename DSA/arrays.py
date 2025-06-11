new_list = [1, 2, 3]
"""This is a list. The values aren't stored in memory and the array 
stores references to each of those objects"""
result = new_list[0]
"""To access a value from an array, the above expression is used. This is a constant time
procedure as the list doesn't have to be gone through, it just checks the offset
from base memory and picks that since we are sure the memory is contiguous. Trying 
to pick an index outside the range gives an index out of range error"""
print(result)

"""Arrays are really fast at accessing, O(1), but bad at searching. Linear search is used
the worst case scenario is therefore linear time or O(n)"""

if 1 in new_list: print(True) #RandomFact- in is a comparison operator
"""This checks if 1 is present in the list"""

for n in new_list:
    if n == 1:
        print(True)
        break
"""This does the same thing, but in a grandiose fashion to illustrate linear search. 
Binary search would need to be sorted which is another operation on it's own so it
might be less efficient"""

#Inserting methods.
#True insert; inserting anywhere in the list. Runtime is linear. Every value has to be affected.
#Appending; adds to the end of the list. Runtime is constant time depending on language implementation.
#Extend; makes a series of append calls on each of the new elements until they've been appended to new list. O(k) where k is number of added elements.
#Delete; shifts every element to the left, opposite of insert. Runtime is linear.

numbers = []
length = len(numbers)
print(length)
"""Python's list is implemented as a dynamic array. Unlike a static array with
fixed size, a dynamic array resizes when needed, like when appending values and 
current allocated space is full. If there's space left, adding an element takes 
O(1) time. For a full list, Python creates a new larger array and copies the existing
elements and then adds the new element. This copying makes some appends take O(n) time.
So basically Python over-allocates extra space to reduce the number of resizing operations
"""
numbers.append(2)
numbers.append(3)
print(len(numbers))
print(numbers)

numbers.extend([4,5,6])
print(numbers)

del numbers[0]
print(numbers)