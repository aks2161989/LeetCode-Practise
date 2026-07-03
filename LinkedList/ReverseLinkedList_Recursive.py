# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        
        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

def printLinkedList(head):
    curr = head
    print('[', end='')
    while curr:
        print(curr.val, end=', ') if curr.next else print(curr.val, end='')
        curr = curr.next
    print(']')

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    sol = Solution()
    result = sol.reverseList(node1)
    printLinkedList(result)




        