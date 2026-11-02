class Queue:
    def __init__(self, name, length = None, queue = None):
        self.name = name
        if queue == None:
            self.upperPointer = 0
            self.lowerPointer = -1
            self.length = length
            self.queue = []
            for _ in range(length):
                self.queue.append(None)

        else:
            # DO LATER

            self.lowerPointer = -1
            for v in queue:
                if v == None:
                    self.lowerPointer += 1 # Flag to realise that it has hit the first value to stop incrementing pointer
                
            self.length = len(queue)
            self.queue = queue

    def isFull(self):
            if self.lowerPointer + 1 == self.upperPointer and self.queue[self.lowerPointer + 1] != None:
                return True
            else:
                return False
    def isEmpty(self):
        if self.queue[self.lowerPointer + 1] == None:
            return True
        else:
            return False
        
    def QueueDeQueue(self):
        if self.isEmpty():
            print(f"ERROR: QUEUE {self.name}({self.queue}) IS EMPTY!")
        else:
            self.queue[self.lowerPointer + 1] = None
            self.lowerPointer += 1
            if self.lowerPointer == self.length - 1:
                self.lowerPointer = -1

    def QueueEnQueue(self,value):
        if not self.isFull():
            self.queue[self.upperPointer] = value
            self.upperPointer += 1
        else:
            print(f"ERROR: QUEUE {self.name}({self.queue}) IS FULL!")
        if self.upperPointer == self.length:
            self.upperPointer = 0

def test():
    myQueue = Queue("myQueue", 6)
    myQueue.QueueDeQueue()
    print(myQueue.lowerPointer)
    print(myQueue.upperPointer)
    myQueue.QueueEnQueue("Hi")
    print(myQueue.queue)
    print(myQueue.lowerPointer)
    print(myQueue.upperPointer)
    myQueue.QueueDeQueue()
    print(myQueue.queue)
    print(myQueue.lowerPointer)
    print(myQueue.upperPointer)

    for _ in range(5):
        myQueue.QueueEnQueue("Hi")
        print(myQueue.queue)
        print(myQueue.lowerPointer)
        print(myQueue.upperPointer)

    for _ in range(8):
        myQueue.QueueDeQueue()
        print(myQueue.queue)
        print(myQueue.lowerPointer)
        print(myQueue.upperPointer)

test()