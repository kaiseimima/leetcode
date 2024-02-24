# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node = set()
        answer_nodes = []
        current_node = head
        while current_node:
            visited_node.add(current_node.val)
            current_node = current_node.next
        print(visited_node)
        return answer_nodes

        
