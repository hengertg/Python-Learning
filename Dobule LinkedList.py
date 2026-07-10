class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None


    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            
            current = current.next

        return None

    def insert(self, node):
        node.next = self.head
        if self.head:
         self.head.previous = None

        self.head = node
        node.previous = None

    def delete(self, node):
        if node.previous is not None:
            node.previous.next = node.next

        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.previous = node.previous

a = Node(10)

b = Node(20)

c = Node (30)

d = Node(40)

a.next = b
b.previous = a
b.next = c
c.previous = b
c.next = d
d.previous = c


print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)