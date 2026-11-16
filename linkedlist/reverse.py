class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_LinkedList(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next 
        current.next = prev
        prev = current
        current = next_node 
    return prev

def display(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
    print("Null")
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("original linkedlist")
display(head)

head = reverse_LinkedList(head)

print("Reveresed linked list")
display(head)