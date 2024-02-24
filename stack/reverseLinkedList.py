# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        stack = []
        rList = ListNode
        while curr_node.next:
            stack.append(curr_node.val)
            curr_node = curr_node.next
        while stack:
            rList.next = stack.pop()
        return rList
        
