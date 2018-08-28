# Prompts the user for a string, checks that it is a corect postfix expression
# built from positive numbers, + and spaces, and if it is,
# outputs a tree representation of the corresponding infix expression.

# Written by *** and Eric Martin for COMP9021


import sys
import re

from array_stack import *
from binary_tree import *


def store_in_two_stacks(expression):
    if any(not (c.isdigit() or c in '+ ') for c in expression):
        return None, None
    tokens = re.findall('(\d+|\+|-|\*|/)', expression)
    if any(token.startswith('0') and token != '0' for token in tokens):
        return None, None
    stack_1, stack_2 = ArrayStack(), ArrayStack()    
    for token in tokens:
        if token == '+':
            stack_1.push(token)
            stack_2.push(token)
        else:
            stack_1.push(int(token))
            stack_2.push(int(token))
    return stack_1, stack_2
            
def stores_correct_postfix_expression(stack):
    if not _stores_correct_postfix_expression(stack):
        return False
    return stack.is_empty()

def _stores_correct_postfix_expression(stack):
    if stack.is_empty():
        return False
    token = stack.pop()
    if token == '+':
        if not _stores_correct_postfix_expression(stack):
            return False
        return _stores_correct_postfix_expression(stack)
    return True

def transfer_from_stack_to_tree(stack):
    if stack.is_empty():
        return BinaryTree()
    token = stack.pop()
    tree = BinaryTree(token)
    if token == '+':
        tree.left_node = transfer_from_stack_to_tree(stack)
        tree.right_node = transfer_from_stack_to_tree(stack)
    return tree


expression = input('Input an expression: ')
if not expression or expression.isspace():
    sys.exit()
stack_1, stack_2 = store_in_two_stacks(expression)
if not stack_1:
    print('Expression not built from nonnegative numbers and +')
else:
    if not stores_correct_postfix_expression(stack_1):
        print('Not a correct postfix expression')
    else:
        tree = transfer_from_stack_to_tree(stack_2)
        tree.print_binary_tree()
        
