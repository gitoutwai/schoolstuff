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

        def QueueDeQueue():
            pass

        def QueueEnQueue():
            pass
        
myQueue = Queue("myQueue", 6)
print(myQueue.queue)