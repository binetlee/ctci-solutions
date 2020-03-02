##https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
##https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/432823/Python-Iterative-Stack-Recursive
##https://www.youtube.com/watch?v=ugBx_T1RHuc
##You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

##Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
##Goal is to use DFS, see the above link for all of the different ways you can flatten a list via DFS
from collections import *
from typing import List


class Solution(object):
    def flatten(self, head):
        temp = head
        stack = []
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                temp2 = head.val
                temp3 = head.next.prev.val
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif not head.next and stack:
                head.next = stack.pop()
                temp4 = head.val
                temp5 = head.next.prev.val
                head.next.prev = head
            head = head.next
        return temp