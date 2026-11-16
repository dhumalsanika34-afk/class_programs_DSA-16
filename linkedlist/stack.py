stack = []
MAX=5
def push(item):
    if len(stack)==MAX:
        print("stack Overflow")
    else:
        stack.append(item)
        print(item,"inserted")
def pop():
            if len(stack)==0:
                print("stack underflow")
            else:
                item=stack.pop()
                print("deleted element:", item)
def peek():
     if len(stack)==0:
          print("stack is empty")
     else:
          print("Top element:",stack[-1])
def display():
               if len(stack)==0:
                    print("stack is empty")
               else:
                    print("stack elements:", stack[::-1])
push(10)
push(20)
push(30)
display()
peek()
pop()
display()