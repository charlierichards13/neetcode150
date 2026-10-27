# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #floyds tortoise and hare

        slow = head
        fast = head


        # while fast and the next node are not null
        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next


            if slow == fast:
                return True
        
        



        #no cycle
        return False