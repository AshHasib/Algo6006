

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        

if __name__=='__main__':
    myQueue=Queue()
    print('Initial size of Queue:', myQueue.size())
    print('Adding some elements :')
    myQueue.enqueue(2)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    myQueue.enqueue(6)
    myQueue.enqueue(98)
    print('Now the size of queue:', myQueue.size())
    print('Removing some elements:')
    myQueue.dequeue()
    myQueue.dequeue()
    print('After removing 2 elements, now the size of the queue is ', myQueue.size())
