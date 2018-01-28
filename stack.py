
#This is the stack class
class Stack:
    
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


if __name__=='__main__':
    
    myStack=Stack()
    
    print('The initial size of my stack is :', myStack.size())
    print('Is the stack empty?')
    print('Answer:', myStack.isEmpty())
    print('Adding 1 to my stack:')
    myStack.push(1)
    print('Displaying Top of my stack:', myStack.peek())
    print('Now adding 34:')
    myStack.push(34)
    print('Now the size of my stack is:', myStack.size())
    print('Now top of my stack has :', myStack.peek())
    print('Adding few more elements:')
    myStack.push(2)
    myStack.push(43)
    myStack.push(65)
    myStack.push(2)
    myStack.push(1)
    
    print('Now the size of my stack is:', myStack.size())
    print('Removing the top element, which is ,' , myStack.pop())
    print('Now the size of the stack is:' , myStack.size())
    print('Is the stack empty?')
    print('Answer:', myStack.isEmpty())
