class Stack:
    def __init__(self, name, length = None, stack = None):
        self.name = name
        if stack == None:
            self.length = length
            self.pointer = -1
            self.stack = []
            for _ in range(length):
                self.stack.append(None)
        else:
            self.length = len(stack)
            self.pointer = -1
            for v in stack:
                if v != None:
                    self.pointer += 1
            self.stack = stack

    def PushStack(self, val):
        if self.pointer >= self.length-1:
            print(f"ERROR: {self.name} IS FULL")
        else:
            self.pointer += 1
            self.stack[self.pointer] = val

    def PopStack(self):
        if self.pointer <= -1:
            print(f"ERROR: {self.name} IS EMPTY")
        else:
            self.pointer -= 1
            self.stack[self.pointer] = None

    def isEmpty(self):
        if self.pointer <= -1:
            return True
        else:
            return False
    
    def PeekStack(self):
        if self.pointer <= -1:
            return f"{self.name} IS EMPTY"
        else:
            return self.stack[self.pointer]

myStack = Stack("myStack", 6)
myStack.PushStack("Hi")
print(myStack.PeekStack())
myStack.PopStack()
myStack.PopStack()
print(myStack.PeekStack())
myStack.PushStack("Hello")
print(myStack.PeekStack())
for _ in range(6):
    myStack.PushStack("Hiiii :)")
print(myStack.PeekStack())
for _ in range(7):
    myStack.PopStack()
print(myStack.isEmpty())

train = Stack("myStack", stack=["A","B","C",None,None])