class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum_stack:
            self.minimum_stack.append(min(self.minimum_stack[-1], val))
        else:
            self.minimum_stack.append(val)

    def pop(self) -> None:
        self.minimum_stack.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
        
