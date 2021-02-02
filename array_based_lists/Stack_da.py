from DynamicArray import *


class StackDA:

    def __init__(self):

        self.data = DynamicArray(1)

    def size(self):

        return self.data.n

    def capacity(self):

        return self.data.capacity

    def push(self, val):

        self.data.add(self.size(), val)

    def pop(self):

        return self.data.remove(self.size()-1)

    def top(self):

        return self.data.get(self.size()-1)


if __name__ == "__main__":

    stack = StackDA()

    for i in range(10):

        stack.push(i)

    print(stack.data)

    for i in range(10):

        print(stack.pop())

    print(stack.data)