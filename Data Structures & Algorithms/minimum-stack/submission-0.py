class MinStack:

    def __init__(self):
        self.stack = []      # main stack
        self.minStack = []   # tracks minimums

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If minStack is empty OR new value is smaller
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # If popped element is the current minimum
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]