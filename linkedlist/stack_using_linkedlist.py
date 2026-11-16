class Node:
 def __init__(self,data):
     self.data= data 
     self.next=None
class Stack:
 def __init__(self):
     self.top=None

 def push(self, items):
    new_node = Node(items)
    new_node.next=self.top
    self.top=new_node
    print(items,"inserted")
 def pop(self):
      if self.top is None:
         print("stack underflow")
      else:
         items= self.top.data
         self.top=self.top.next
         print("Deleted element:", items)
 def peek(self):
    if self.top is None:
       print("stack is empty")
    else:
       print("top element:", self.top.data)
 def display(self):
    if self.top is None:
       print("Stack is Empty")
    else:
       temp=self.top
       print("Stack elements:")
       while temp is not None:
          print(temp.data)
          temp=temp.next
s =Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()