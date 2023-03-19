class Queue:
    
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def push(self,x):
        self.s1.append(x)

    def pop(self,x):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):    
        if not self.s1 and not self.s2:    
            return True
    