# Written by **** for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        len1 = len(self)
        smallest = self.head.value
        n = 1
        node = self.head

        while node.next_node:
            if smallest>node.next_node.value:
                smallest = node.next_node.value
            node = node.next_node
        # select index of min value of L
        smallest_node = self.index_of_value(smallest)


        node = self.head
        while node and node.next_node:
            node = node.next_node
        node.next_node = self.head

        i = 0
        head1 = node
        if smallest_node:

            while i != smallest_node:
                head1 = node.next_node
                node = head1
                i += 1

        self.head = head1.next_node
        #lnode:left node rnode:right node
        lnode = self.head
        while n != len1 / 2:
            node = lnode.next_node
            rnode = node.next_node
            lnode.next_node = head1
            head1.next_node = rnode
            head1 = node
            lnode = rnode
            n += 1
        lnode.next_node = head1
        head1.next_node = None

