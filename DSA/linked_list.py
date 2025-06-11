class Node:
    """An object for storing a single node of a linked list.
    Models 2 attributes; data and the link to the next node in the list.
    """
    data = None  # Default value for data
    next_node = None  # Default reference to next node (None means no next node)

    def __init__(self, data):
        self.data = data  # Assigns provided data when creating a new node

    def __repr__(self):
        return "<Node data: %s>" % self.data  # String representation for debugging


class LinkedList:
    """Singly linked list"""

    def __init__(self):
        self.head = None  # Default value for data

    def is_empty(self):
        return self.head is None

    def size(self):
        """Return the size of the linked list by counting the number of nodes in list"""
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """Adds a new node containing data at head of the list
        Takes constant time, which is the best case scenario
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """Search for the first node containing data that matches the key
        Returns the node or 'None' if not found

        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point
        takes O(n), therefore taking overall O(n) time.
        """
        if index == 0:
            self.add(data)
            return  # Prevent further execution

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1 and current is not None:
                current = current.next_node
                position -= 1

            if current is None:  # Handle out-of-bounds index
                raise IndexError("Index out of range")

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """Removes node containing data that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node  # removes previous head

            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                current.next_node = None

            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head

        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """Return a string representation of the linked list. Takes O(n)"""

        nodes = []
        current = self.head

        while current is not None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "->".join(nodes)


l = LinkedList()
l.add(1)
print(l.size())
l.add(2)
l.add(3)
print(l.search(3))