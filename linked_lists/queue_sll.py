from SLList import *

class QueueSLL:

	def __init__(self):

		self.sll = SinglyLinkedList()

	def head(self):

		return self.sll.head

	def tail(self):

		return self.sll.tail

	def enqueue(self, val):

		self.sll.add(self.sll.size, val)

	def dequeue(self):

		return self.sll.remove(0)

if __name__ == "__main__":

    queue = QueueSLL()

    for i in range(10):
        queue.enqueue(i)

    print(queue.sll)
    print(queue.sll.size)
    for i in range(10):
        print(queue.dequeue().val)
        print(queue.sll.size)
        print(queue.sll)