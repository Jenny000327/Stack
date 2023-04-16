class Stack:
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

S = Stack()
S.push(10)
S.push(2)
print(S.top())
print(S.pop())
print(len(S))
print(S.isEmpty())