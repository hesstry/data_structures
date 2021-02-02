class SinglyLinkedListQueue:

  def __init__(self):

    self.head = None
    self.tail = None
    self.size = 0

  def append(self, x):

    node = Node(x)

    tail = self.tail

    if self.size == 0:

      self.head = node

    else:

        tail.next = node

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