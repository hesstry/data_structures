class NodeDoubly:
    """
    Doubly-linked node class for doubly-linked list
    """
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLListException(Exception):
    pass


class DoublyLinkedList:

    def __init__(self):
        """
        parameters:
            None

        attributes:
            self.head(Object): the head of the list

            self.tail(Object): the tail of the list

            self.size(Int): size of the list

            self.dummy(Node): dummy node to indicate ends
        """

        self.head = None
        self.tail = None
        self.size = 0
        self.dummy = NodeDoubly(None)

    def get(self, i):
        """
        parameters:
            i(int): Index of item to retrieve

        returns:
            val(Object): the i'th element of the SLList

        functionality:
            retrieves the node at the specified index
        """
        try:
            if self.size == 0 or i < 0 or i >= self.size:
                raise DLListException

            node = self.head

            for loop in range(i):
                node = node.next

            return node

        except DLListException:
            print("***DLList Exception***\nList empty or invalid index")

    def set(self, i, val):
        """
        parameters:
            i(int): Index for desired element to change
            x: value to change element to

        returns:
            node.val if set properly

            DLList exception otherwise

        functionality:
            sets value of specified index with specified value
        """
        try:
            if i < 0 or i >= self.size:
                raise DLListException

            node = self.get(i)

            node.val = val

        except DLListException:
            print("***DLList Exception***\n***Invalid Index***")

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
                raise DLListException

            new_node = NodeDoubly(val)

            if self.size == 0:
                self.head = new_node
                self.dummy.next = self.head
                self.head.prev = self.dummy
                self.tail = new_node
                self.tail.next = self.dummy
                self.dummy.prev = self.tail
                self.size += 1
                return

            if i == 0:
                new_node.next = self.head # make new node point to current head
                self.head.prev = new_node # make current head.prev point to new head
                self.dummy.next = new_node # make self.dummy point to new_node
                new_node.prev = self.dummy
                self.head = new_node # make new_node self.head
                self.size += 1
                return

            if i == self.size:
                self.tail.next = new_node # make current tail point to new tail
                new_node.prev = self.tail # make new tail prev point to current tail
                self.tail = new_node # assign new node as tail
                self.tail.next = self.dummy # point new tail to self.dummy
                self.dummy.prev = self.tail # point dummy.prev to new tail
                self.size += 1
                return

            left_adj_node = self.get(i - 1)
            right_adj_node = left_adj_node.next
            left_adj_node.next = new_node
            new_node.prev = left_adj_node
            new_node.next = right_adj_node
            right_adj_node.prev = new_node
            self.size += 1

        except DLListException:
            print("***DLList Exception***\n***Invalid Index***")

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
                raise DLListException

            if i == 0:
                new_head = self.head.next
                removed = self.head
                self.head = new_head
                self.dummy.next = new_head
                new_head.prev = self.dummy
                self.size -= 1
                return removed

            if i == self.size - 1:
                new_tail = self.tail.prev
                removed = self.tail
                self.tail = new_tail
                self.tail.next = self.dummy
                self.dummy.prev = new_tail
                self.size -= 1
                return removed

            left_adj_node = self.get(i - 1)
            removed = left_adj_node.next
            right_adj_node = removed.next
            left_adj_node.next = right_adj_node
            right_adj_node.prev = left_adj_node
            self.size -= 1
            return removed

        except DLListException:
            print("***DLList Exception***\n***List empty or invalid index***")

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

    dll = DoublyLinkedList()

    for i in range(10):
        dll.add(i, i)

    print(dll)

    for i in range(10):
        print(dll.remove(i).val)
        print(dll)
