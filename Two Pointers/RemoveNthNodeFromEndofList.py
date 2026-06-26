# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for i in range(n+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast= fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
    
def printNode(head: Optional[ListNode]):
    print('[', end="")
    node = head
    while node is not None:
        print(node.val, end=", ") if node.next else print(node.val, end="")
        node = node.next
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

    sol = Solution()
    printNode(sol.removeNthFromEnd(node1, 2))