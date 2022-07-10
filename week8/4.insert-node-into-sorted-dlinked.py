#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

# create dummy = prev
# while curr and curr.data < data:
# tranverse 

# prev and current
# prev.next = new, new.prev = prev
# new.next = current
# current.prev = new, 
def sortedInsert(llist : DoublyLinkedListNode, data : int) -> DoublyLinkedListNode:
    if not llist:
        return DoublyLinkedList(data) 
    
    prev = dummy = DoublyLinkedListNode(0)
    prev.next = curr = llist
    while curr and curr.data < data:
        prev = prev.next
        curr = curr.next
    # found the loc
    new_node = DoublyLinkedListNode(data)
    prev.next = new_node
    new_node.prev = prev
    new_node.next = curr
    if curr:
        curr.prev = new_node
    
    return dummy.next
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
