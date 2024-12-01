class Stack:
    def __init__(self):
        """ initializes an empty stack and sets it size
            data fields: 
                stack: a python list as the internal data structure
                size: a counter to keep track of the size of the stack 
        """
        self.stack: list = []
        self.size: int = 0

    def push(self, item) -> None:
        """ puts the item on top of the stack and adjusts the stack size"""
        self.stack.insert(0, item)
        self.size += 1

    def pop(self) -> int:
        """ removes and returns the item on top of the stack
            also adjusts the stack size accordingly
            if the stack is empty, an Exception should be raise
        """
        top = self.stack.pop(0)
        if (self.size) > 0:
            self.size -= 1
        else:
            raise Exception ("The stack is empty")
        
        return top 

    def peek(self):
        """ returns the item on top of the stack without affecting it
            if the stack is empty, returns None
        """
        if (self.size) > 0:
            return self.stack[0]
        else:
            raise Exception ("The stack is empty")
            
    def getSize(self):
        """ returns the size of the stack"""
        return self.size

#Testing: 
#   instantiate a stack object
s = Stack()
#   call push to push 1
s.push(1)
#   call push to push "one"
s.push("one")
#   call peek and print the returned item
print(s.peek())
#   call pop and print the returned item
print(s.pop())
#   call getSize and print the returned value
print(s.getSize())