
#The Deque class
class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def isPalindrome(str):
    myDeque=Deque()
    
    for ch in str:
        myDeque.addRear(ch)
    stillOk=True
    
    while myDeque.size()>1 and stillOk:
        first=myDeque.removeFront()
        last=myDeque.removeRear()
        
        if first!=last:
            stillOk=False
    return stillOk
    
if __name__=='__main__':
    
    str=input('Enter a string:')
    if isPalindrome(str):
        print('The string is palindrome')
    else:
        print('The string is not palindrome')
        
