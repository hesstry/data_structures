class SinglyLinkedListStack:

  def __init__(self):

    self.head = None
    self.tail = None
    self.size = 0

  def push(self, x):

    node = Node(x)

    node.next = self.head

    self.head = node

    if self.size == 0:

      self.tail = node

    self.size += 1

  def pop(self):

    if self.size == 0:
        return None

    val = self.head

    self.head = val.next

    self.size -= 1

    return val

  def list_print(self):

    start = self.head

    for i in range(self.size):

      print(start.val)

      start = start.next


class Node:

  def __init__(self, val):

    self.val = val
    self.next = None