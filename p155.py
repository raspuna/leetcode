class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self, val):
        if self.stack:
            self.stack.append([val, min(val, self.stack[-1][1])])
        else:
            self.stack.append([val, val])
            
    def pop(self):
        if self.stack:
            self.stack.pop(-1)
    def top(self):
        if len(self.stack) < 1:
            return None
        else :
            return self.stack[-1][0]
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None