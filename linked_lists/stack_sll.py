from SLList import *

class StackSLL:

	def __init__(self):

		self.sll = SinglyLinkedList()

	def top(self):

		return self.sll.head

	def push(self, val):

		self.sll.add(0, val)

	def pop(self):

		return self.sll.remove(0)

if __name__ == "__main__":

	stack = StackSLL()

	for i in range(10):
		stack.push(i)

	print(stack.sll)
	print(stack.sll.size)
	for i in range(10):
		print(stack.pop().val)
		print(stack.sll)
		print(stack.sll.size)