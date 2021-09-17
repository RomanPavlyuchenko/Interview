class Stack:
    data = None

    def __init__(self, init_list=None):
        if init_list is None:
            init_list = []
        self.data = init_list.copy()

    def is_empty(self):
        return bool(not self.data)

    def push(self, new_elem):
        self.data.append(new_elem)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)
