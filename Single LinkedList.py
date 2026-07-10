class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        pass


a = Node(20)

b = Node(30)

c = Node(40)

d = Node(50)

f = Node(60)

a.next = b

b.next = c

c.next = d

d.next = f

print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)
print(a.next.next.next.next.data)