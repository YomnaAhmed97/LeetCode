# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative solution with two pointers
#         Initialize two points, fast pointer will move to the next and next node while slow pointer only moves one node. When the fast pointer move into the last node, the slow pointer is the
        ptr1 = head # steady (slow)
        ptr2 = head # moving pointer (fast)
        while ptr2 != None and ptr2.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return ptr1