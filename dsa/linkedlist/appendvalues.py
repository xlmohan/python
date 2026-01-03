class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_values(self, values):
        for value in values:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

ll = LinkedList()
ll.append_values([1, 2, 3, 4, 5])
print(ll.display())  # Output: [1, 2, 3, 4, 5]