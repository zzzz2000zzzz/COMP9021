# Prompts the user for a string, checks that it is a corect postfix expression
# built from positive numbers, + and spaces, and if it is,
# outputs a tree representation of the corresponding infix expression.

# Written by *** and Eric Martin for COMP9021


import sys
import re

from array_stack import *
from binary_tree import *


def store_in_two_stacks(expression):
    return None, None
    # Replace above line with your code 
            
def stores_correct_postfix_expression(stack):
    pass
    # Replace pass above with your code 

def transfer_from_stack_to_tree(stack):
    pass
    # Replace pass above with your code 

# Possibly define other functions

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
        
