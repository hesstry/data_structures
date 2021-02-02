from DynamicArray import *


class QueueDA:

    def __init__(self):

        self.data = DynamicArray(1)

    def size(self):

        return self.data.n

    def capacity(self):

        return self.data.capacity

    def enqueue(self, val):

        self.data.add(self.size(), val)

    def dequeue(self):

        return self.data.remove(0)


if __name__ == "__main__":

    queue = QueueDA()

    for i in range(10):

        queue.enqueue(i)

    print(queue.data)

    for i in range(10):

        print(queue.dequeue())

    print(queue.data)