# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []

        # Add the head of every non-empty list
        for list_index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(
                    min_heap,
                    (node.val, list_index, node)
                )

        dummy = ListNode()
        tail = dummy

        while min_heap:
            _, list_index, node = heapq.heappop(min_heap)

            #Attach the smallest available node.
            tail.next = node
            tail = tail.next

            #Add the next node from the same linked list
            if node.next is not None:
                heapq.heappush(
                    min_heap,
                    (node.next.val, list_index, node.next)
                )

        return dummy.next

def printLinkedList(head):

    print('[', end="")
    while head:
        print(head.val, end=", ") if head.next else print(head.val, end="")
        head = head.next
    print("]")

if __name__ == "__main__":
    l1n1 = ListNode(1)
    l1n2 = ListNode(4)
    l1n3 = ListNode(5)
    l1n1.next = l1n2
    l1n2.next = l1n3
    l1n3.next = None

    l2n1 = ListNode(1)
    l2n2 = ListNode(3)
    l2n3 = ListNode(4)
    l2n1.next = l2n2
    l2n2.next = l2n3
    l2n3.next = None

    l3n1 = ListNode(2)
    l3n2 = ListNode(6)
    l3n1.next = l3n2
    l3n2.next = None
  
    sol = Solution()
    result = sol.mergeKLists([l1n1, l2n1, l3n1])
    printLinkedList(result)



        