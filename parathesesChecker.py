
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
        
def isBalanced(str):
    s=Stack()
    balanced=True
    index=0
    
    while index<len(str) and balanced:
        symbol=str[index]
        
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index+=1
    if s.isEmpty() and balanced:
        return True
    else:
        return False

if __name__=='__main__':
    
    str1='(()())'
    str2='(()))'
    print('For 1st string:' ,  isBalanced(str1))
    print('For 2nd string:' ,  isBalanced(str2))
