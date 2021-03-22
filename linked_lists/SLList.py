class NodeSingly:
    """
    A singly-linked node, used for the Singly-Linked List
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class SLListException(Exception):
    pass


class SinglyLinkedList:

    def __init__(self):
        """
        parameters:
            None

        attributes:
            self.head(Object): the head of the list

            self.tail(Object): the tail of the list

            self.size(Int): number of elements in the list
        """
        self.head = None
        self.tail = None
        self.size = 0
        self.dummy = NodeSingly(None)

    def get(self, i):
        """
        parameters:
            i(int): Index of item to retrieve

        returns:
            val(Object): the i'th element of the SLList

        functionality:
            Simple get method for retrieving items of the list given some index
        """
        try:
            if self.size == 0 or i < 0 or i >= self.size:
                raise SLListException

            node = self.head

            for loop in range(i):
                node = node.next

            return node

        except SLListException:
            print("***SLList Exception*** \n***List empty or invalid index***")

    def set(self, i, val):
        """
        parameters:
          i(int): Index for desired element to change
          x: value to change element to

        returns:
          node.val if set properly

          SLList exception otherwise

        functionality:
          simple set method for an element given some index
        """
        try:
            if i < 0 or i > self.size - 1:
                raise SLListException

            node = self.get(i)
            node.val = val

        except SLListException:
            print("***SLList Exception***\n***Invalid Index***")

    def add(self, i, val):
        """
        parameters:
            i(int): index to add value at

            val(object): value of new node to add

        returns:
            None

        functionality:
            adds new node at specified index, making sure proper linkage is preserved
        """
        try:
            if i < 0 or i > self.size:
                raise SLListException

            new_node = NodeSingly(val)

            if self.size == 0:
                self.head = new_node
                self.dummy.next = self.head
                self.tail = new_node
                self.tail.next = self.dummy
                self.size += 1
                return

            if i == 0:
                new_node.next = self.head
                self.dummy.next = new_node
                self.head = new_node
                self.size += 1
                return

            if i == self.size:
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = self.dummy
                self.size += 1
                return

            left_adj_node = self.get(i - 1)
            right_adj_node = left_adj_node.next
            left_adj_node.next = new_node
            new_node.next = right_adj_node
            self.size += 1

        except SLListException:
            print("***SLList Exception***\n***Invalid Index***")

    def remove(self, i):
        """
        parameters:
            i(int): index to remove value at

        returns:
            removed(object): removed value

        functionality:
            removes node at specified index, preserving proper linkage
        """
        try:
            if i < 0 or i >= self.size or self.size == 0:
                raise SLListException
                return

            if i == 0:
                new_head = self.head.next
                removed = self.head
                self.head = new_head
                self.dummy.next = new_head
                self.size -= 1
                return removed

            if i == self.size - 1:
                new_tail = self.get(self.size - 1)
                removed = self.tail
                self.tail = new_tail
                new_tail.next = self.dummy
                self.size -= 1
                return removed

            adj_node = self.get(i - 1)

            removed = adj_node.next

            self.size -= 1

            adj_node.next = removed.next

            return removed

        except SLListException:
            print("***SLList Exception*** \n***List empty or invalid index***")

    def __str__(self):
        if self.size == 0:
            return "[]"

        str_list = "["

        curr_node = self.head

        while curr_node != self.dummy:
            if curr_node.next == self.dummy:
                str_list += (str(curr_node.val) + "]")
            else:
                str_list += (str(curr_node.val) + ", ")
            curr_node = curr_node.next

        return str_list


if __name__ == "__main__":

    sll = SinglyLinkedList()

    for i in range(10):
        print(sll)
        sll.add(i, i)

    print(sll)

    for i in range(10):
        print(sll.remove(i).val)
        print(sll)
