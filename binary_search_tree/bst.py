import sys
sys.path.append('/Users/trystenhess/Desktop/CS/CS261/data_structures/linked_lists')

from linked_lists import queue_sll, stack_sll, SLList


class TreeNode:
    """
    Node to be used for the BST
    """
    def __init__(self, val):
        """
        p = parent
        left = left child
        right = right child
        """
        self.parent = None
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return self.val


class BST:

    def __init__(self):
        self.root = None
        self.node_count = 0

    def __str__(self):
        """
        Prints the tree as an array in breadth-first order
        """
        printed = "PRE ORDER: {}\nIN ORDER: {}\nPOST ORDER: {}".format(self.pre_order_traversal(), self.in_order_traversal(), self.post_order_traversal())
        return printed

        # node_queue = queue_sll.QueueSLL()
        #
        # if self.root is not None:
        #     node_queue.enqueue(self.root)
        #
        # tree = "["
        #
        # while node_queue.sll.size > 0:
        #
        #     curr_node = node_queue.dequeue().val
        #     tree += (str(curr_node.val) + ", ")
        #
        #     # accounts for all child nodes
        #     if curr_node.left:
        #         node_queue.enqueue(curr_node.left)
        #
        #     if curr_node.right:
        #         node_queue.enqueue(curr_node.right)
        #
        # # remove extra comma and space
        # tree = tree[:-2]
        # tree += "]"
        # return tree

    def find(self, val):
        """
        parameters:
            val

        returns:
            found node or none

        functionality:
            finds the first occurrence of the node with the specified value, returns none if not found
        """

        curr_node = self.root

        while curr_node is not None:
            if val < curr_node.val:
                curr_node = curr_node.left

            elif val > curr_node.val:
                curr_node = curr_node.right

            else:
                return curr_node

        return curr_node

    def find_last(self, val):
        """
        parameters:
            val

        returns:
            last occurrence of node with specified val, or the would-be parent of a node if it contained
            the specified val

        functionality:
            finds where the node with the specified val is, or the parent of the node if it did exist
        """

        curr_node = self.root
        parent_node = None

        while curr_node is not None:
            parent_node = curr_node

            if val < curr_node.val:
                curr_node = curr_node.left

            elif val > curr_node.val:
                curr_node = curr_node.right

            # if they are equal, return the found node
            else:
                return curr_node

        # if the node isn't found, return its would-be parent
        return parent_node

    def depth(self, node):
        """
        parameters:
            node(Object): a node in the tree

        returns:
            d(int): the depth of the specified node

        functionality:
            finds depth of nodes within the tree
        """

        d = 0

        while node != self.root:
            node = node.parentarent
            d += 1

        return d

    def size(self, node):
        """
        parameters:
            node(Object): a node in the tree

        returns:
            size of subtree with specified node as the root

        functionality:
            counts the number of nodes within the subtree rooted at the specified node
        """

        s = 0

        node_queue = queue_sll.QueueSLL()
        node_queue.enqueue(node)

        while node_queue.sll.size > 0:

            curr_node = node_queue.dequeue()
            s += 1

            # accounts for all child nodes
            if curr_node.left:
                node_queue.enqueue(curr_node.left)

            if curr_node.right:
                node_queue.enqueue(curr_node.right)

        return s

    def in_order_traversal(self):

        in_order_stack = []
        in_order_length = 0

        if self.root is None:
            return in_order_stack

        curr_node = self.root
        previous = None

        while in_order_length < self.node_count:

            # first time getting to curr_node
            if previous == curr_node.parent:
                # go left if we can, to smallest node
                if curr_node.left is not None:
                    next = curr_node.left
                # else go right if we can, this means curr_node is smallest within local subtree rooted at curr_node
                # append curr_node to in_order_stack
                elif curr_node.right is not None:
                    in_order_stack.append(curr_node.val)
                    in_order_length += 1
                    next = curr_node.right
                # if no left and no right node, then move on to the next subtree later in traversal order
                # append this node to the in_order_stack list
                else:
                    in_order_stack.append(curr_node.val)
                    in_order_length += 1
                    next = curr_node.parent

            # this is the next node in line to be appended since it comes right after curr_node.left in terms of ordering
            elif previous == curr_node.left:
                in_order_stack.append(curr_node.val)
                in_order_length += 1

                if curr_node.right is not None:
                    next = curr_node.right

                else:
                    next = curr_node.parent

            # if we've reached here that's because we have finished visiting this subtree and must move on
            else:
                next = curr_node.parentarent

            previous = curr_node
            curr_node = next

        return in_order_stack

    def pre_order_traversal(self):
        """
        parameters:
            none

        returns:
            pre-order traversal of the BST

        functionality:
            much like in-order traversal, except nodes are accounted for the moment they are reached
        """
        pre_order_stack = []
        pre_order_length = 0

        if self.root is None:
            return pre_order_stack

        curr_node = self.root
        previous = None

        while pre_order_length < self.node_count:

            # first time getting to curr_node
            # append each time we reach a new node for pre-ordering
            if previous == curr_node.parent:
                pre_order_stack.append(curr_node.val)
                pre_order_length += 1

                if curr_node.left is not None:
                    next = curr_node.left

                elif curr_node.right is not None:
                    next = curr_node.right

                else:
                    next = curr_node.parent

            elif previous == curr_node.left:

                if curr_node.right is not None:
                    next = curr_node.right

                else:
                    next = curr_node.parent

            # if we've reached here that's because we have finished visiting this subtree and must move on
            else:
                next = curr_node.parentarent

            previous = curr_node
            curr_node = next

        return pre_order_stack

    def post_order_traversal(self):
        """
        parameters:
            none

        returns:
            pre-order traversal of the BST

        functionality:
            much like in-order traversal, except nodes are accounted for after reaching them for the final time

            basically once we move from a node to its parent, we are leaving the node, and it should be accounted
            for
        """

        post_order_stack = []
        post_order_length = 0

        if self.root is None:
            return post_order_stack

        curr_node = self.root
        previous = None

        while post_order_length < self.node_count:

            # first time getting to curr_node
            if previous == curr_node.parent:
                # go left if we can, to smallest node
                if curr_node.left is not None:
                    next = curr_node.left
                # else go right if we can, this means curr_node is smallest within local subtree rooted at curr_node
                elif curr_node.right is not None:
                    next = curr_node.right
                # if no left and no right node, then move on to the next subtree later in traversal order
                else:
                    post_order_stack.append(curr_node.val)
                    post_order_length += 1
                    next = curr_node.parent

            elif previous == curr_node.left:

                if curr_node.right is not None:
                    next = curr_node.right

                else:
                    post_order_stack.append(curr_node.val)
                    post_order_length += 1
                    next = curr_node.parent

            # if we've reached here that's because we have finished visiting this subtree and must move on
            else:
                post_order_stack.append(curr_node.val)
                post_order_length += 1
                next = curr_node.parent

            previous = curr_node
            curr_node = next

        return post_order_stack

    def add(self, val):
        """
        parameters:
            val(Object): value to give new node

        returns:
            boolean dictating whether or not node was added

        functionality:
            checks to see if a node already contains this value, if so, returns false, if not,
            adds to node with specified value and returns true
        """

        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
            self.node_count += 1
            return

        searched_node = self.find_last(val)

        if searched_node.val == val:
            return False

        # this executes if the node doesn't exist
        if val > searched_node.val:
            searched_node.right = new_node

        elif val < searched_node.val:
            searched_node.left = new_node

        new_node.parent = searched_node
        self.node_count += 1
        return True

    def remove(self, val):
        """
        parameters:
            val(object): value of node to be removed

        returns:
            true if removed, false otherwise

        functionality:
            finds node with specified value and removes it, returns true, if not found, returns false
        """



if __name__ == '__main__':
    to_add = [1, 5, 3, 6, 2, 6, 3]

    bst = BST()

    for num in to_add:
        bst.add(num)

    print(bst)