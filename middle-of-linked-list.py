# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow_p = head
        fast_p = head

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        return slow_p
