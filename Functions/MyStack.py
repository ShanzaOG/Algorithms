#My Stack file

class MyStack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def push(self,item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

