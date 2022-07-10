#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

# create dummy head
# loop until either of node is None
# if node1 is Node, append the rest of Node 2
# else : append the rest of Node 1
# return dummy next


def mergeLists(head1: SinglyLinkedListNode, head2: SinglyLinkedListNode) -> SinglyLinkedListNode:
    current_node = dummy_head = SinglyLinkedListNode(0)
    while head1 or head2:
        if head1 and head2:
            if head1.data < head2.data:
                current_node.next = head1
                head1 = head1.next
            else:
                current_node.next = head2
                head2 = head2.next
        elif head1 and not head2:
            current_node.next = head1
            head1 = head1.next

        else:
            current_node.next = head2
            head2 = head2.next

        current_node = current_node.next

    return dummy_head.next


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
