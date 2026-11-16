
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(a, b):
    dummy = Node(0)
    c = dummy

    while a is not None and b is not None:
        if a.data <= b.data:
            c.next = a
            a = a.next
        else:
            c.next = b
            b = b.next

        c = c.next


    if a is not None:
        c.next = a
    else:
        c.next = b

    return dummy.next


def display(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

c = merge(a, b)

print("Merged linked list:")
display(c)
