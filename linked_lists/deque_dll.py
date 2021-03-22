from DLList import *

class DequeDLL:

    def __init__(self):
        self.DLL = DoublyLinkedList()

    def add_front(self, val):
        self.DLL.add(0, val)

    def remove_front(self):
        return self.DLL.remove(0)

    def add_end(self, val):
        self.DLL.add(self.DLL.size, val)

    def remove_end(self):
        return self.DLL.remove(self.DLL.size-1)

    def __str__(self):
        return self.DLL.__str__()

if __name__ == "__main__":

    deque = DequeDLL()

    for i in range(10):
        deque.add_front(i)

    print(deque)

    for i in range(10):
        deque.add_end(i)

    print(deque)

    for i in range(10):
        print(deque.remove_front().val)
        print(deque)

    for i in range(10):
        print(deque.remove_end().val)
        print(deque)
