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
        
def hotPotato(nameList, numPasses):
    simQueue=Queue()
    for name in nameList:
        simQueue.enqueue(name)
    
    while simQueue.size()>1:
        for i in range(numPasses):
            simQueue.enqueue(simQueue.dequeue())
        simQueue.dequeue()
    return simQueue.dequeue()
    
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
