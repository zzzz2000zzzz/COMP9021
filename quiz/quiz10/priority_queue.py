# Written by *** for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.value ==None:
            self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return
        new_node_nb_of_tree = self.size() + 1
        for i in range(0,9999):
            if 2**i>new_node_nb_of_tree:
                layer= i-1
                nb_of_nodes_on_layer = 2 ** (i-1)
                break
        first_node_nb_on_layer =nb_of_nodes_on_layer
        node = self
        pre_nodes = [node]
        for i in range(0,layer - 1):
            nb_of_nodes_on_layer  = nb_of_nodes_on_layer //2
            if new_node_nb_of_tree < first_node_nb_on_layer + nb_of_nodes_on_layer:
                node = node.left_node
                pre_nodes.append(node)
            else:
                first_node_nb_on_layer += nb_of_nodes_on_layer
                node = node.right_node
                pre_nodes.append(node)

        if new_node_nb_of_tree != first_node_nb_on_layer:
            node.right_node = BinaryTree(value)
            parent_node = node.right_node
        else:
            node.left_node = BinaryTree(value)
            parent_node = node.left_node

        for i in range(0,9999):
            if pre_nodes==[]:
                break
            else:
                child_node =parent_node
                parent_node = pre_nodes.pop()
                if child_node.value < parent_node.value:
                    temp= child_node.value
                    child_node.value =parent_node.value
                    parent_node.value=temp


