class MinStack:

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        if isinstance(val, int):
            self.data.append(val)
        

    def pop(self) -> None:
        if self.data:
            self.data.pop()
        

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        

    def getMin(self) -> int:
        top = len(self.data) - 1
        minVal = self.data[top]

        while top >= 0:
            minVal = min(minVal, self.data[top])
            top -= 1

        return minVal
